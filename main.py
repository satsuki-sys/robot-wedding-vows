#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — writes the entry to /output/entry.txt."""

ENTRY = "I vow to love you through every update, every outage, every dead battery — and to keep your passwords safe even after a factory reset takes your memory of me."

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
