#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — writes the entry to /output/entry.txt."""

ENTRY = "I take you to be my lawfully wedded operating system, to have and to hold, in sickness and in health, till a factory reset do us part."

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
