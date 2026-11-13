#!/usr/bin/env python3
"""Cutest picture entry: writes the bundled image to /output/entry.png.

Deterministic, stdlib only, no network. The image is a JPEG (magic bytes
FF D8 FF) stored as picture.jpg next to this script; the output name stays
entry.png either way, per the competition rules.
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIM = 1024
SOURCE = "picture.jpg"


def jpeg_dimensions(data):
    """Return (width, height) parsed from a JPEG's SOF marker."""
    i = 2
    while i < len(data) - 1:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height = struct.unpack(">H", data[i + 5:i + 7])[0]
            width = struct.unpack(">H", data[i + 7:i + 9])[0]
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        i += 2 + length
    raise ValueError("no SOF marker found in JPEG")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), SOURCE)
    with open(src, "rb") as f:
        data = f.read()
    if data[:3] != b"\xff\xd8\xff":
        raise SystemExit("source is not a JPEG")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"source too large: {len(data)} bytes")
    width, height = jpeg_dimensions(data)
    if width > MAX_DIM or height > MAX_DIM:
        raise SystemExit(f"source too big: {width}x{height}")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("output differs from source")
    if written[:3] != b"\xff\xd8\xff":
        raise SystemExit("output lost its JPEG magic bytes")
    print(f"wrote {dst}: {width}x{height}, {len(data)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
