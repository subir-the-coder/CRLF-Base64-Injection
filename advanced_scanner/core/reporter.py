import json
import os
from datetime import datetime

def save_report(target, results):
    os.makedirs("advanced_scanner/reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    txt_path = f"advanced_scanner/reports/report-{timestamp}.txt"
    json_path = f"advanced_scanner/reports/report-{timestamp}.json"

    with open(txt_path, "w") as f:
        f.write(f"CRLF Scan Report\nTarget: {target}\n\n")
        for entry in results:
            f.write(f"Payload: {entry['payload']}\n")
            f.write(f"Status: {entry['status']}\n")
            f.write(f"Headers: {entry['headers']}\n\n")

    with open(json_path, "w") as f:
        json.dump(results, f, indent=4)

    return txt_path, json_path
