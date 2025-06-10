import csv
import pathlib
import random
import chess
import time
import argparse, sys

def show_board(board: chess.Board) -> None:
    print(board.unicode(borders = True))
    print()

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

def prompt_move(board: chess.Board) -> chess.Move | None:

    raw = input("Your move (or 'q' to quit):").strip()
    if raw.lower() in {"q"}:
        return None
    
    try:
        move = chess.Move.from_uci(raw)
    except ValueError:
        try:
            move = board.parse_san(raw)
        except ValueError:
            move = None
    if move is None or move not in board.legal_moves:
        print("Illegal move!! Try again\n")
        return prompt_move(board)
    return move

def run_session(puzzles: list[tuple[chess.Board, chess.Move]], n:int) -> None:

    correct = 0
    for i in range(1, n + 1):
        board, best = random.choice(puzzles)
        print("\n" + "-" * 40)
        print(f"Puzzle {i}/{n}")
        show_board(board)
        
        move = prompt_move(board)
        if move is None:
            break
        
        if move == best:
            print("Correct!!!!")
            correct += 1
        else:
            print(f"WRONG -- the best move was {best.uci()}\n")
            
        time.sleep(0.60)
        
    print("=" * 40)
    print(f"Session complete: {correct}/{i} correct " f"({correct/i: .0%})")
    
def main() -> None:
    parser = argparse.ArgumentParser(description="CLI chess tactics trainer. Made with love in Python without any frameworks")

    parser.add_argument("--csv", default="puzzles_subset.csv", help = "Path to the Lichess CSV (edited)")
    parser.add_argument("--puzzles", type=int, default=10, help="Number of puzzles to attempt")
    parser.add_argument("--puzzles", type=int, default=10, help="Number of puzzles to attempt")
    parser.add_argument("--min-rating", type=int, help="Skip puzzles below this rating")
    parser.add_argument("--max-rating", type=int, help="Skip puzzles above this rating")
    parser.add_argument("--theme", type=int, help="Filter by Lichess theme (fork, matein2, etc.)")

    args = parser.parse_args()
    
    try:
        puzzles = load_lichess_csv(
            args.csv,
            max_rows = args.puzzles * 5, # load more for randomness
            min_rating = args.min_rating,
            max_rating = args.max_rating,
            theme = args.theme
        )
    except FileNotFoundError:
        sys.exit("CSV not found")
        
    if not puzzles:
        sys.exit("No puzzles match your filters")    
        
    run_session(puzzles, args.puzzles)
    
    if __name__ == "__main__":
        main()