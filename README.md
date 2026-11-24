# One-Line Roast: The Gadget You Use Every Day

[![make.fun](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/reren-dev/roast-the-gadget-01/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/reren-dev/roast-the-gadget-01/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

An entry for the [One-Line Roast: The Gadget You Use Every Day](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610) bounty on [make.fun](https://make.fun).

`main.py` writes one original roast line (at most 200 characters) about a
gadget used every day to `entry.txt` in the output directory given by
`MAKEFUN_OUTPUT_DIR`. Python 3.13 standard library only — no network, no
wall clock. The line is validated (single line, 1–200 characters, no
leading/trailing whitespace), written atomically via a fixed temp name and
`os.replace`, chmodded to 0644, then read back and verified.

## The line

> My left earbud dies mid-call every single day, and the right one keeps playing in mono, smug, like it's already auditioning for a solo career.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
