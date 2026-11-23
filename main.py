#!/usr/bin/env python3
"""Deterministically copy the bundled 1024x1024 poster to MAKEFUN_OUTPUT_DIR."""

import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> None:
    payload = SOURCE.read_bytes()
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / OUTPUT_NAME).write_bytes(payload)


if __name__ == "__main__":
    main()
