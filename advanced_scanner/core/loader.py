import os

def load_payloads(path):
    payloads = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")

                # skip only fully empty lines
                if line.strip() == "":
                    continue

                # DO NOT skip comments
                # DO NOT skip HTML
                # DO NOT skip script tags
                # DO NOT skip chains
                # DO NOT skip text lines
                
                payloads.append(line)

        return payloads

    except FileNotFoundError:
        print(f"[!] Payload file not found: {path}")
        return []



def load_targets():
    print("\nEnter targets (one per line). Press ENTER twice to finish:\n")
    targets = []
    while True:
        url = input("> ").strip()
        if url == "":
            break
        targets.append(url)
    return targets
