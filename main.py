#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes one funny smart-speaker apology (after mishearing its owner) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = (
    "Apologies. You said 'remind me at nine'; I heard 'rewind time.' "
    "I cannot do that, so I have simply lowered my confidence in both of us."
)


MAX_CHARS = 140


def validate(text: str) -> None:
    """Gate check, mirroring the kit: 1-140 UTF-8 chars, one line, not only whitespace."""
    text.encode("utf-8")  # raises on non-UTF-8-encodable content
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character in the file,
    # so the file content is exactly ENTRY.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
