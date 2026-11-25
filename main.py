"""Funniest Autocorrect Fail — make.fun entry.

Writes one line to /output/entry.txt that reads as a hilarious
autocorrect fail: an apology for being late, where the phone turned
"meeting at noon" into "melting at noon", and now the boss thinks the
sender is a candle. The fail is the message, and the message is the
fail.
"""

import os

ENTRY = (
    "Sorry I am late, my ducking autocorrect changed meeting at noon "
    "to melting at noon and now my boss thinks I am a candle, so I "
    "am working from home until I solidify."
)

MAX_CHARS = 199


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
