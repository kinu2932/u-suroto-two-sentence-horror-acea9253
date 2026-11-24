"""Two-sentence horror entry for make.fun.

Writes exactly one two-sentence horror story to entry.txt, with no
trailing newline. The story is a constant: the program takes no input,
makes no network calls, and is fully deterministic.
"""

import os

ENTRY = (
    "My husband started sleepwalking last month, so I tied a small brass "
    "bell to his ankle to wake me when he gets up. "
    "Last night the bell rang twice from the hallway, and when I opened my "
    "eyes, he was fast asleep beside me, the bell still tied to his ankle, silent."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
