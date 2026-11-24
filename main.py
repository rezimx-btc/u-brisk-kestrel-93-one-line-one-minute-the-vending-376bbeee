#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

A vending machine flirting with a passing human. One line, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = (
    "You pressed B4 for a soda, but I dispensed a date instead \u2014 "
    "error 418, I'm short-circuiting over your smile."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
