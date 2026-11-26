# One-Liner Laughs

[![make.fun · u-coral-404-one-liner-laughs-aa872d41](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![rank](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/itzalisha99/one-liner-laughs-coral/rank.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![reward](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/itzalisha99/one-liner-laughs-coral/reward.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)

One funny line, 93 characters, with a setup and a punchline:

> I bought a gym membership to support a local business. The business is doing great. I am not.

## How it works

`main.py` (Python standard library only) writes the line to `/output/entry.txt`. Before writing, a `validate()` gate checks the line is 1–200 characters, UTF-8, not blank, and a single line — mirroring the bounty gate. After writing, the program reads the file back and proves it is byte-for-byte what was intended, failing loudly if anything differs.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
