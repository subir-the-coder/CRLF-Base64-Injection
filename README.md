# 🔥 CRLF + Base64 Injection Proof of Concept

**Author:** Subir Sutradhar  
**Project Type:** Research + Exploit PoC  
🕶 Cybersecurity | 🔍 Vulnerability Research  

---

## 📌 Overview

This repository demonstrates a vulnerability where an attacker can exploit a **CRLF (Carriage Return Line Feed)** injection to manipulate response headers.

When combined with **Base64 encoding**, some filters fail, allowing payloads to bypass sanitization.

![587464582_122172854942387183_4863059669732189671_n](https://github.com/user-attachments/assets/ec16c720-f0b0-4bef-a54f-35c8189afb2b)

---


## 🚀 Features

- Encoded / Decoded payloads
- Header injection PoC
- Works with vulnerable query parameters
- Cookies, CSP, cache poisoning attack vectors

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing only.**
Unauthorized use is illegal.

---

## 📁 Files Included

| File | Description |
|------|------------|
| exploit.py | Main PoC script |
| payloads.txt | Test payloads |
| poc.txt | Vulnerability explanation |
| LICENSE | APache license |
