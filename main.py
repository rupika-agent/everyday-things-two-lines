"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of a queue to /output/entry.txt:
line 1 explains the everyday thing to a 10-year-old in one vivid
sentence built on an analogy; line 2 says in one sentence why the
analogy works, what it maps and what it leaves out.
"""

ENTRY_LINES = [
    "A queue is like the lunch line on pizza Friday, where 200 kids "
    "shuffle forward one tray at a time and nobody gets served just "
    "because they're the hungriest.",
    "The analogy works because both run on strict first-come-first-served "
    "order, but it leaves out the pizza smell and the teacher on "
    "line-cutter duty, so in a real queue the only guard is two hundred "
    "strangers staring at you.",
]


def main():
    text = "\n".join(ENTRY_LINES) + "\n"
    assert 1 <= len(text.strip()) <= 400, "entry must be 1-400 chars"
    assert len(ENTRY_LINES) == 2, "entry must be exactly two lines"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
