"""make.fun entry: Everyday Things, Two Lines, Longer Run.

Explains an everyday thing -- a queue -- in exactly two lines,
using the lunch line on pizza Friday as the analogy.
Deterministic: fixed text only, no randomness, no time, no network.
The two lines are kept verbatim in ENTRY_LINES; do not reword them.
"""

ENTRY_LINES = [
    "A queue is like the lunch line on pizza Friday, where 200 kids shuffle forward one tray at a time and nobody gets served just because they're the hungriest.",
    "The analogy works because both run on strict first-come-first-served order, but it leaves out the pizza smell and the teacher on line-cutter duty, so in a real queue the only guard is two hundred strangers staring at you.",
]


def main() -> None:
    text = "\n".join(ENTRY_LINES) + "\n"
    stripped = text.strip()
    assert 1 <= len(stripped) <= 400
    assert len(stripped.splitlines()) == 2
    assert len(ENTRY_LINES) == 2
    import os

    # Create the output directory if needed, then write the entry file.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
