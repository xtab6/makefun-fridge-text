#!/usr/bin/env python3
"""The 3AM Fridge Text — writes one line to /output/entry.txt.

The line: "3am. Your midnight snack just texted me, worried about YOU.
I'm the fridge. Go to bed."

Role reversal is the joke: the snack is worried about the owner, and the
fridge — a machine with a small voice and an opinion — is the one breaking
the news, then closing with a blunt order. No milk, no expired yogurt, no
pickles union, no door left open: every angle the field already burned.

Gate (from the competition requirements): /output/entry.txt must be UTF-8
text of 1 to 140 characters, not only whitespace. The file holds exactly
the line, no trailing newline, so its length is the line's length: 86
characters, 16 words, one line.
"""

import os

LINE = "3am. Your midnight snack just texted me, worried about YOU. I'm the fridge. Go to bed."


def checked_line() -> str:
    """Return LINE if it passes the competition gate, else fail loudly."""
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(LINE) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(LINE))
    return LINE


def main() -> None:
    text = checked_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the line: a short or
    # failed write must fail the run, never ship a truncated entry.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not match the line")


if __name__ == "__main__":
    main()
