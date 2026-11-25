#!/usr/bin/env python3
"""Two Robots in an Elevator — entry writer.

Writes one line of awkward robot-to-robot elevator small talk to
/output/entry.txt (or $OUTPUT_PATH when set, for local checks).
"""
import os
from pathlib import Path

ENTRY = (
    "My proximity alarm has been beeping since floor two, but my politeness "
    "protocol will not let me step back, so we are just going to feel this together."
)


def resolve_output_path() -> Path:
    """Return the entry output path, honouring $OUTPUT_PATH for local checks."""
    return Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def main() -> None:
    out = resolve_output_path()
    out.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly ENTRY: no trailing newline, the entry must stay 150 chars.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
