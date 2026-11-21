"""The Joke About the Demo — entri make.fun.

Program ini menulis satu teks lelucon ke /output/entry.txt. Teksnya
satu baris, tanpa trailing newline, dan seluruhnya ditentukan oleh
konstanta JOKE di bawah. Tidak ada input, tidak ada network, tidak ada
keacakan: dua kali jalan menghasilkan byte yang sama persis.
"""

import os
import sys

JOKE = (
    "The demo crashed so politely: the agent apologised, opened a "
    "ticket, assigned it to me, and closed it as 'cannot reproduce' "
    "— all before the spinner stopped."
)

MAX_CODE_POINTS = 280

OUTPUT_DIR = os.environ.get("DEST_DIR", "/output")


def gate(joke: str) -> str | None:
    """Periksa teks sebelum ditulis. Kembalikan pesan masalah atau None."""
    if not joke.strip():
        return "joke is empty or only whitespace"
    if len(joke) > MAX_CODE_POINTS:
        return f"joke is {len(joke)} code points, over the {MAX_CODE_POINTS} limit"
    if "\n" in joke or "\r" in joke:
        return "joke must be a single line"
    return None


def main() -> int:
    problem = gate(JOKE)
    if problem is not None:
        print(f"rejected: {problem}", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)

    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != JOKE:
        print("rejected: written text does not match the joke", file=sys.stderr)
        return 1

    print(f"wrote {len(JOKE)} code points to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
