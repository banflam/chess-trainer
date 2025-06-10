import csv
import pathlib
import random
import chess

def load_lichess_csv(path: str| pathlib.Path, max_rows: int| None = None, min_rating: int | None = None, max_rating: int | None = None, theme: str | None = None) -> list[tuple[chess.Board, chess.Move]]: