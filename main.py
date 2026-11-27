"""Moon-answers-back entry: emit the Moon's one-line comeback."""

import os

LINE = "Stop howling at me. I'm a rock with good lighting, not your therapist."


def main() -> None:
    if "\n" in LINE or not 1 <= len(LINE) <= 240:
        raise ValueError("entry must be a single line of 1 to 240 characters")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
