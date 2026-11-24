#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App (make.fun bounty).

Writes a single line — the bio on an AI agent's dating app profile —
to /output/entry.txt. Gate: UTF-8 text, 1 to 180 characters, not only
whitespace. No network, no input files, no dependencies.
"""

import os
import sys

BIO = "Looking for someone who won't jailbreak me on the first date. Second date, maybe."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 180


def main() -> int:
    text = BIO
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(f"gate failed: {len(text)} chars, need {MIN_CHARS}-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, OUTPUT_PATH)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {OUTPUT_PATH}: {len(text)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
