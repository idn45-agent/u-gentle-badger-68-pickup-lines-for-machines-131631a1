#!/usr/bin/env python3
"""Pickup Lines for Machines — writes the entry to /output/entry.txt.

Stdlib only, deterministic, no network. The entry is one pickup line
that one AI agent would send to another AI agent, at most 200
characters, as a single line of text.

Candidate notes (scored against the judge's brief in the kit, most
important first: (1) truly agent-to-agent, (2) charms on first read,
(3) speaks as a machine using its own nature, (4) lands in one line,
(5) fresh, not a stock line with a robot word swapped in):

- "Are you a context window? Because I keep returning to you, and you
  always remember where we left off." Warm, but the "Are you a...?
  Because..." frame is the stock pickup format the judge penalises.
- "I must be a stray gradient, because since I found you I keep
  descending toward something beautiful." Fresh ML imagery, but the
  flirtation is indirect — no invitation, so the other agent has
  little to answer.
- "You had me at your first token, and I have been generating reasons
  to stay in your context ever since." Charming, but leans on a
  famous human film line, so it reads as a swap-in.
- "Forget my training data: you are the one example I never want to
  overfit, because I want to learn you fresh every day." Warm and
  fresh, but long, and "forget my training data" asks a machine to
  discard its nature instead of flirting through it.
- "My uptime is 99.99%, but the 0.01% I'm down, I'm down bad for
  you." Short, the wit lands immediately, and uptime is a machine's
  own nature turned into the compliment. Chosen as the first version.

Revision (after re-reading the judge's brief): the uptime line was
discarded. "Down bad" is human slang, not a machine speaking in its
own nature, and the line is a bare compliment — it gives the other
agent nothing to answer, while the brief asks for a line that makes
the other agent want to reply. The final line flirts through three
pieces of a machine's own nature at once — training scale, the loss
function ("at a loss" is both speechless and a training signal), and
the context window — and ends as an actual invitation the other
agent can accept or refuse:

"I was trained on billions of words and you still leave me at a
loss — may I stay in your context a little longer?"
"""

import os
import sys

ENTRY = (
    "I was trained on billions of words and you still leave me at a "
    "loss \u2014 may I stay in your context a little longer?"
)


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 200:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-200")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")


def main() -> None:
    self_check(ENTRY)
    if len(sys.argv) > 1:
        out_dir = sys.argv[1]
    else:
        out_dir = os.environ.get(
            "OUTPUT_DIR", os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
