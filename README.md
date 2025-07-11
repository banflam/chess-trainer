# Chess Tactics Trainer -- a pure Python CLI

Practice chess puzzles from the comfort of the command line.

Small, lightweight program with no major external dependencies.

Written from scratch in 129 lines of Python and without any framework, just for the challenge.

---

## Features

| ✔ | What it does |
|---|--------------|
| **CC-0 puzzle data** | Uses a tiny 1 k-row slice of the official Lichess puzzle DB (4 M positions) |
| **Rating & theme filters** | `--min-rating 1600 --theme fork` |
| **Side-to-move banner** | Clear “White to move” / “Black to move” every round |
| **Colourized ASCII board** | Unicode pieces + ANSI colours, readable in any terminal |
| **Instant feedback** | Correct / Wrong with best-move answer |
| **No frameworks** | Only external package is `python-chess` |

---

## Quick start

```bash
# 1 – new virtual environment
python -m venv .venv
source .venv/bin/activate

# 2 – install dependency
pip install -r requirements.txt

# 3 – train!
python chess_trainer.py --puzzles 20

## Example CLI flags

python chess_trainer.py \
       --puzzles 30 \
       --min-rating 1500 \
       --max-rating 2100 \
       --theme fork

# Origins of the puzzles

1,000 puzzles randomly sampled from the CC-0 Lichess puzzle database
