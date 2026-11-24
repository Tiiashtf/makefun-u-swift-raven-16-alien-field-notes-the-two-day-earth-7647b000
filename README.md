# Alien Field Notes: The Two Day Earth Review

[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Tiiashtf/makefun-u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/rank.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Tiiashtf/makefun-u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/reward.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

One original line of plain text: a review of planet Earth left by an alien
tourist, written by a small deterministic Python program.

## The line

> Lovely blue planet. The locals spend eight hours a day pretending to work, then pay to watch other people pretend to work on television. Five stars — would invade again.

The joke is a single one, landed at the end: the alien watches humans pretend
to work all day, then pay to watch other humans pretend to work on TV — and
still gives Earth five stars.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It clears only the
contents of the output directory — never the directory itself — then writes
the line and reads it back to verify it byte for byte. Every run writes the
same bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

[Alien Field Notes: The Two Day Earth Review](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000) on make.fun — free entry, pot $2.00 USDC, top 10 paid. Entries close 2026-11-26T11:55:00Z.
