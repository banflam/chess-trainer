import csv
import pathlib
import random
import chess

def load_lichess_csv(path: str| pathlib.Path, max_rows: int| None = None, min_rating: int | None = None, max_rating: int | None = None, theme: str | None = None) -> list[tuple[chess.Board, chess.Move]]:
    puzzles: list[tuple[chess.Board, chess.Move]] = []

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if min_rating and int(row["Rating"]) < min_rating:
                continue
            if max_rating and int(row["Rating"]) > max_rating:
                continue
            if theme and theme not in row["Themes"].split():
                continue

            board = chess.Board(row["FEN"])
            moves = row["Moves"].split()
            board.push_uci(moves[0])
            best_move = chess.Move.from_uci(moves[1])
            
            puzzles.append((board, best_move))
            
            if max_rows and len(puzzles) >= max_rows:
                break
    return puzzles

