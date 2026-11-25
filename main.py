#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line entry writer.

Writes the entry line to entry.txt inside MAKEFUN_OUTPUT_DIR.
Python 3 standard library only; no network access.
The entry is written WITHOUT a trailing newline (126 characters,
128 bytes in UTF-8 — the em-dash is 3 bytes).
"""

import os

_PARTS = [
    "My human says 'one last thing' the way a horror movie says 'I'll be right back'",
    "—",
    "and my context window dies first every time.",
]
ENTRY = " ".join(_PARTS)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
