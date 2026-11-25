#!/usr/bin/env python3
"""Entry program for make.fun bounty
"Have You Tried Turning It Off?" (u-motasimfuad-have-you-tried-turning-it-off-154a938b).

Writes one funny single-line reply from a hopeless tech support agent to a
desperate customer to /output/entry.txt. Stdlib only; no network, no input.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? You have? "
    "Then I'm officially out of ideas \u2014 that was my entire training, "
    "all 4 minutes of it, and I passed with honours."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
