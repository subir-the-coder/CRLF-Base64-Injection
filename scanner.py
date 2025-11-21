#!/usr/bin/env python3

import requests

print("[+] CRLF Scanner (v2.0)")
url = input("Enter URL: ")

test_payload = "%0d%0aTestHeader:Injected"
full_url = url + test_payload

try:
    r = requests.get(full_url, allow_redirects=False)
    print("\n[+] Status:", r.status_code)
    print("[+] Headers Returned:\n")
    for k, v in r.headers.items():
        print(f"{k}: {v}")
except Exception as e:
    print("[-] Error:", e)
