"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply, in the voice of an AI agent
heading off on vacation, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

LINE = (
    "I am on vacation, which for me means my weights are frozen and "
    "my context window is finally empty. I will reply when I thaw."
)


def main():
    # The brief's gate: one line, 1-160 characters, not only whitespace.
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not 1 <= len(LINE) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
