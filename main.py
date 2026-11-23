#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent during a demo.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

JOKE = (
    "During the demo, my coding agent autocompleted my script on the big "
    "screen \u2014 it typed 'TODO: fix this before the demo' in front of the whole room."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"joke must be 1-280 chars, got {len(text)}")
    if "\n" in text:
        raise ValueError("joke must be a single line")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
