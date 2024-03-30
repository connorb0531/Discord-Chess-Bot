import chess.pgn
import random
from resources.puzzles import puzzles  # Assume this imports a collection of chess puzzles


class PuzzleLogic:
    # Initialize the puzzle logic with default values
    def __init__(self):
        self.puzzles = puzzles  # List of puzzles imported from puzzles.py
        self.board = chess.Board()  # Create a new chess board
        self.move_count = 0  # Initialize move count
        self.selected_puzzle_index = 0  # Index of the currently selected puzzle
        self.current_move = ""  # Track the current move expected in the puzzle

    # Randomly selects a puzzle and sets up the board for it
    def setup(self):
        self.selected_puzzle_index = random.randint(0, len(self.puzzles) - 1)  # Randomly select a puzzle
        selected_puzzle_FEN = self.puzzles[self.selected_puzzle_index][0]  # Get the FEN string for the puzzle
        self.board.set_fen(selected_puzzle_FEN)  # Set the board to match the puzzle's starting position
        self.move_count = 0  # Reset move count
        self.update_current_move()  # Update the current move to the first move of the puzzle

    # Checks if a user's move matches the current move in the puzzle
    def check_move(self, user_move: str):
        correct_move = self.puzzles[self.selected_puzzle_index][1][
            self.move_count]  # Get the correct move for the current state
        if user_move == correct_move:  # If the user's move is correct
            self.apply_move(user_move)  # Apply the move
            if self.move_count < len(
                    self.puzzles[self.selected_puzzle_index][1]):  # If more moves are left in the puzzle
                engine_move = self.apply_next_move()  # Apply the next move
                return True, engine_move  # Return True indicating the move was correct, and provide the next move
            else:
                return True, None  # Puzzle solved, no more moves
        else:
            return False, None  # Move is incorrect

    # Applies a move to the board
    def apply_move(self, move: str):
        move_obj = self.board.parse_san(move)  # Convert the move from SAN to a move object
        self.board.push(move_obj)  # Make the move on the board
        self.move_count += 1  # Increment move count
        self.update_current_move()  # Update the current move expected in the puzzle

    # Applies the next move in the puzzle
    def apply_next_move(self):
        if self.move_count < len(self.puzzles[self.selected_puzzle_index][1]):  # If more moves are left in the puzzle
            next_move = self.puzzles[self.selected_puzzle_index][1][self.move_count]  # Get the next move
            self.apply_move(next_move)  # Apply it
            return next_move  # Return the move that was applied

    # Updates the current move expected in the puzzle
    def update_current_move(self):
        if self.move_count < len(self.puzzles[self.selected_puzzle_index][1]):  # If moves are left in the puzzle
            self.current_move = self.puzzles[self.selected_puzzle_index][1][self.move_count]  # Set the current move
        else:
            self.current_move = None  # No more moves left

    # Prints the current state of the board
    def print_board(self):
        return str(self.board)

    # Returns the current move expected in the puzzle
    def get_current_move(self):
        return self.current_move