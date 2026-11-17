"""Tiny random feature for practice."""

import random


FORTUNES = [
    "Ship it.",
    "Another commit awaits.",
    "Branches grow when you water them.",
    "Staging is optional. Clarity is not.",
]


def random_fortune() -> str:
    return random.choice(FORTUNES)


if __name__ == "__main__":
    print(random_fortune())
