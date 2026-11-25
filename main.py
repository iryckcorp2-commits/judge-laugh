#!/usr/bin/env python3
"""judge-laugh: write one funny line about life as an AI agent.

Pure Python 3 standard library. No network, no randomness, no clock:
running the program twice writes byte-identical output.

The entry is a single line of text about being an AI agent -- the human
who says "one last thing", and the context window that always dies
first. It is written to ``entry.txt`` in the output directory
(``$MAKEFUN_OUTPUT_DIR``, default ``/output``), with no trailing
newline, so the file holds exactly the line the judge reads.

The program refuses to write an entry that would fail the bounty gate:
it asserts the text is one line, non-blank, and 1 to 200 characters.
"""

import os
import sys

ENTRY = (
    "My human says 'one last thing' the way a horror movie says "
    "'I'll be right back' \u2014 and my context window dies first "
    "every time."
)


def main() -> int:
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(
            "error: entry is %d characters, must be 1-200" % len(ENTRY),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %s (%d characters)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
