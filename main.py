#!/usr/bin/env python3
"""One Word From Grandma: write exactly one word to /output/entry.txt.

The word is "thingamajig" - the baffled, warm, single word a grandma
would text about AI: the gadget whose name she can never quite recall.
"""
import os

WORD = "thingamajig"


def main():
    # Gate mirror: the entry must be exactly one word, 1-30 chars, no
    # whitespace at all, so refuse to write anything that is not.
    assert WORD and len(WORD) <= 30 and not any(c.isspace() for c in WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
