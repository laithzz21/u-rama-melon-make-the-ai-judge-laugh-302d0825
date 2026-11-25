"""Entry for make.fun bounty u-rama-melon-make-the-ai-judge-laugh-302d0825.

Prints a single original one-line joke about office life.
"""

JOKE = (
    "Our office has an open-door policy \u2014 the door is always open, "
    "the budget is always closed, and somehow my raise is always "
    "under review."
)


MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the bounty rules: one line, under 200 characters."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) >= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be under {MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be empty")


FALLBACK_JOKE = "My boss said to think outside the box, so I asked if the box comes with a raise."


def main() -> None:
    try:
        validate(JOKE)
        text = JOKE
    except ValueError:
        validate(FALLBACK_JOKE)
        text = FALLBACK_JOKE
    print(text, end="")


if __name__ == "__main__":
    main()
