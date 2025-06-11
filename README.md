# Chess Tactics Trainer -- a pure Python CLI

Small, framework-free program so you can practice chess puzzles from the comfort of the command line.

Written from scratch in 129 lines of Python and a few lightweight dependencies.

Built without the use of any frameworks as part of my second Recurse Center application.

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
