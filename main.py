"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (at most 200 characters) about a
gadget used every day to entry.txt in the output directory given by
MAKEFUN_OUTPUT_DIR. Python 3.13 stdlib only; no network, no wall clock.
"""

import os

MAX_CHARS = 200

ROAST = (
    "My left earbud dies mid-call every single day, and the right one keeps "
    "playing in mono, smug, like it's already auditioning for a solo career."
)


def validate(line: str) -> str:
    """Check the line against the gate: 1-200 chars, one line, not blank."""
    if not line or not line.strip():
        raise ValueError("roast line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"roast line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if line != line.strip():
        raise ValueError("roast line must not start or end with whitespace")
    return line


def main() -> None:
    line = validate(ROAST)
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.replace(tmp_path, path)
    os.chmod(path, 0o644)
    # Read it back and verify what landed on disk.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("entry.txt on disk does not match the roast line")
    validate(written)


if __name__ == "__main__":
    main()
