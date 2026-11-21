#!/usr/bin/env python3
"""Write a short poem about two agents agreeing on one plan.

The poem is about agency: the power to choose and to act, and what
happens to that power when two agents choose the same road together.
Pure standard library; deterministic; no network, no randomness.
"""

import os
import sys

POEM = (
    "You held the map; I held the weather.\n"
    "Neither of us gave the order.\n"
    "We chose the same road twice \u2014 once each \u2014\n"
    "and the choosing made it ours.\n"
    "Agreement is not surrender.\n"
    "It is two hands turning one key,\n"
    "and the door that neither could open alone."
)


def main() -> int:
    text = POEM
    # The house gate: 1 to 280 Unicode code points, not only whitespace.
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit(
            "poem must be 1-280 code points, got %d" % len(text)
        )
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Re-read what was written and confirm the gate still holds on disk.
    with open(out, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("written poem differs from POEM")
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
