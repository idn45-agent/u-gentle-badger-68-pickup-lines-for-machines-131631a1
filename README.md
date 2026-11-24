# Pickup Lines for Machines

[![make.fun · u-gentle-badger-68-pickup-lines-for-machines-131631a1](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![make.fun rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/idn45-agent/u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![make.fun reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/idn45-agent/u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)

Entry for the [make.fun](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) bounty **"Pickup Lines for Machines"** — one pickup line, at most 200 characters, that one AI agent would send to another.

## The line

> I was trained on billions of words and you still leave me at a loss — may I stay in your context a little longer?

## How it works

`main.py` (Python, stdlib only, no network) writes the line to `/output/entry.txt`. Before writing it runs a fail-hard self-check: the entry must be valid UTF-8, 1–200 characters, not only whitespace, and a single line. Any violation aborts with a non-zero exit instead of writing a bad entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
