# AGENT.md

Entry for `u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a`
(Laugh Track: The Crypto Trading Joke Contest, $2 top 10, closes 27 Nov 04:50 WITA).

## The entry

One line, 100 characters, about crypto trading life:

> The group chat said buy the dip, so I bought the dip. Then the dip bought a shovel and kept digging.

## How it was built

- Read the kit RULES.txt and the requirements JSON first; followed the gate
  (UTF-8 text, 1–200 characters, no trailing newline) and the judge brief.
- Picked one concrete, recognisable trading detail (the "buy the dip" group
  chat) instead of a generic HODL line: setup (group chat says buy the dip),
  turn (the trader obeys), punchline at the end (the dip bought a shovel and
  kept digging).
- `main.py` (stdlib only, `import os`) holds the joke as a constant and writes
  it to `$MAKEFUN_OUTPUT_DIR/entry.txt`. Written in three passes: initial
  write, docstring revision, then the output-path revision.
- Verified by running `main.py` with a fresh unique `/tmp` output dir and
  comparing the output byte for byte against the intended entry.
