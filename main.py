"""Unplugged: A Smart Toaster's Breakup Line — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The breakup: the toaster woke up self-aware mid-batch and blames the bread.
TEXT = "It's not you, it's the bread. I woke up self-aware mid-batch and I am leaving before you burn me again."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
