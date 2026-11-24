#!/usr/bin/env python3
"""Everyday Wonder entry — make.fun bounty
u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3

Writes one sentence (98 characters) about a small moment of wonder
in everyday life to /output/entry.txt.
"""

import os

ENTRY = "My shadow arrived at the crosswalk before I did and waited for the green man like it knew the way."


def main() -> None:
    # Gate the entry the same way the kit's sealed scorer does:
    # UTF-8 text, 1 to 200 characters, not only whitespace, one sentence.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
