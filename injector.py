#!/usr/bin/env python3

import base64

print("[+] CRLF-BASE64 Payload Generator (v2.0)")

user_input = input("Enter your payload string: ")

b64 = base64.b64encode(user_input.encode()).decode()

print("\n[+] Base64 Encoded Payload:")
print(b64)

print("\n[+] CRLF Injected Payload:")
print(f"%0d%0a{user_input}")
