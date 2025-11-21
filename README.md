🚀 CRLF & Base64 Injection Scanner v2.0

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/922f5236-438c-400b-a99e-c005919e1b1c" />



# CRLF & Base64 Injection Scanner v2.0

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Version](https://img.shields.io/badge/Release-v2.0-orange)
![Security](https://img.shields.io/badge/Security-Research%20Tool-red)



Advanced asynchronous CRLF + Base64 Injection Scanner built with aiohttp, designed for security researchers and penetration testers.

This tool automates header injection testing, supports custom payloads, and generates detailed TXT + JSON reports for every target.

🧩 Features

🔥 Asynchronous scanning (super fast)

🧪 CRLF injection detection

🔐 Base64 payload support

📡 Header reflection detection (hacker=owned)

📁 Custom payload file support

📜 TXT + JSON report generation

🧵 Massive parallel request execution

🎨 Ascii banner (pyfiglet powered)

⚠ Redirect blocking for clean results

🧰 Modular structure (core/, banners/, advanced_scanner/)

# 📦 Installation

-- git clone https://github.com/<your-username>CRLF_Base64-Injection.git
|  cd CRLF_Base64-Injection
| pip3 install -r requirements.txt


🛠 Usage

Basic command:

python3 advanced_scanner/scanner.py -u "https://postman-echo.com/response-headers?foo=" --payloads advanced_scanner/payloads.txt


Arguments:

| Flag          | Description                                |
| ------------- | ------------------------------------------ |
| `-u`, `--url` | Base URL to test (must end with parameter) |
| `--payloads`  | Path to payload file                       |

🎯 Example Targets to Test

Perfect for injection testing:
https://postman-echo.com/response-headers?foo=
These endpoints reflect headers back — ideal for CRLF testing.

📄 Reports

After each scan you get:

/reports/<domain>/<timestamp>.txt
/reports/<domain>/<timestamp>.json

Each report includes:

Payload used

Server response

Headers returned

Detected injections

⚠ Legal Disclaimer

This tool is for educational and authorized security testing only.
I am not responsible for misuse.

✨ Author

Gray Code (Subir)
Pentester • Security Researcher • Automation Dev
