"""One-Liner Laughs — one funny line, written to /output/entry.txt.

The line: a gym membership bought as charity, with the punchline that the
only thing getting a workout is the business's bank balance.
"""

import os

LINE = "I bought a gym membership to support a local business. The business is doing great. I am not."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back and prove the file is byte-for-byte what was intended.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise RuntimeError("output does not match the intended line")
    validate(written)
    print("verified", path, len(LINE), "chars")


if __name__ == "__main__":
    main()
