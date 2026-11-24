#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text - a review of planet Earth left by
an alien tourist - to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only. No network. Deterministic: every run writes the same bytes.
"""

import os
import shutil
import sys

LINE = (
    "Lovely blue planet. The locals spend eight hours a day pretending to "
    "work, then pay to watch other people pretend to work on television. "
    "Five stars \u2014 would invade again."
)


def clear_contents(path):
    """Remove everything inside path, never path itself."""
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.islink(target) or os.path.isfile(target):
            os.unlink(target)
        elif os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.unlink(target)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    clear_contents(out_dir)
    entry_path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    # Write atomically: a crash mid-write can never leave a partial file.
    tmp_path = entry_path + ".tmp"
    with open(tmp_path, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, entry_path)
    # Read back and verify byte for byte, and as valid UTF-8 text.
    with open(entry_path, "rb") as f:
        back = f.read()
    if back != data:
        print("verification failed: entry.txt differs from intended bytes",
              file=sys.stderr)
        return 1
    if back.decode("utf-8") != LINE:
        print("verification failed: entry.txt is not the intended UTF-8 text",
              file=sys.stderr)
        return 1
    if not (1 <= len(LINE) <= 200):
        print("verification failed: line length out of range", file=sys.stderr)
        return 1
    if "\n" in LINE or LINE.strip() == "":
        print("verification failed: line must be a single non-blank line",
              file=sys.stderr)
        return 1
    print(f"wrote {len(data)} bytes to {entry_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
