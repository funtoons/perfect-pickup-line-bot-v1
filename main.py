"""The Perfect Pickup Line.

Writes a single short pickup line an AI agent could say out loud to a
person, to /output/entry.txt. Deterministic and offline: the line is a
constant, no randomness, no network, no timestamps.
"""

import os

LINE = "I ran a million simulations, and in every one of them, you smiled back."


def main():
    # The gate accepts 1-200 characters of UTF-8 text; fail loudly
    # instead of submitting an over-long line.
    assert 1 <= len(LINE) <= 200, "pickup line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
