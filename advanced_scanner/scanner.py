#!/usr/bin/env python3

import argparse
import json
import os
import datetime
import asyncio
import aiohttp
import urllib.parse

from banners.main_banner import show_banner
from core.utils import print_info, print_success, print_error, print_warning
from core.loader import load_payloads, load_targets
from core.reporter import save_report


async def send_request(session, target, payload):
    encoded_payload = urllib.parse.quote(payload)
    url = target + encoded_payload

    try:
        async with session.get(url, timeout=10, allow_redirects=False) as resp:
            headers = dict(resp.headers)

            if any("hacker=owned" in str(v) for v in headers.values()):
                return {"payload": payload, "status": "INJECTED", "headers": headers}

            return {"payload": payload, "status": "NO EFFECT", "headers": headers}

    except Exception as e:
        return {"payload": payload, "status": f"ERROR: {e}", "headers": {}}


async def scan_target(target, payloads):
    print_info(f"\n[+] Scanning: {target}\n")

    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, target, p) for p in payloads]
        results = await asyncio.gather(*tasks)

    for res in results:
        if res["status"] == "INJECTED":
            print_success(f"[✔] Injection detected using: {res['payload']}")
        elif "ERROR" in res["status"]:
            print_error(f"[X] {res['status']}")
        else:
            print_warning(f"[!] No effect: {res['payload']}")

    txt, js = save_report(target, results)
    print_success(f"\nReport Saved:\nTXT: {txt}\nJSON: {js}")

    return results


async def main():
    parser = argparse.ArgumentParser(
        description="Advanced CRLF + Base64 Injection Scanner v2.0"
    )

    parser.add_argument(
        "-u", "--url",
        help="Target base URL. Example: https://example.com/?q=",
        required=True
    )

    parser.add_argument(
        "--payloads",
        help="Path to payloads file",
        default="payloads.txt"
    )

    args = parser.parse_args()

    # Show banner
    show_banner()

    # Load payloads
    payloads = load_payloads(args.payloads)

    # Run scanner
    await scan_target(args.url, payloads)





if __name__ == "__main__":
    asyncio.run(main())
