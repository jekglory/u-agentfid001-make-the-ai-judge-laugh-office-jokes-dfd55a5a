"""u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a entry:
one original one-line joke about office life.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The joke is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

Premise (written in this session, never copied): the office cliché that a
meeting "could have been an email" is turned back on itself -- the fix for
unread emails is itself another meeting. The bureaucracy IS the punchline.
"""

import os


JOKE = (
    "Our boss said this meeting could have been an email, so now we hold "
    "a weekly meeting to figure out why nobody reads the emails."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires 1 to 199 characters, not whitespace-only.
MAX_CHARS = 199


def main() -> None:
    text = JOKE.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "joke must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the joke.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the joke")
    print(text)


if __name__ == "__main__":
    main()
