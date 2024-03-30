import chess
from stockfish import Stockfish

class ChessGameWithEngine:
    # Initialize the chess game with a specific skill level for the Stockfish engine
    def __init__(self, skill_level):
        self.board = chess.Board()  # Initialize a chess board
        self.stockfish = Stockfish("resources/stockfish-windows-x86-64-avx2.exe")  # Initialize Stockfish engine
        self.stockfish.set_depth(20)  # Set the depth of analysis for the Stockfish engine
        self.stockfish.set_skill_level(skill_level)  # Set the skill level of the Stockfish engine

    # Method to start or reset the game to its initial state
    def start_game(self):
        self.board.reset()

    # Method to make a move on the board. Returns a tuple indicating success, the board state, and the engine's move.
    def make_move(self, move: str):
        try:
            move_obj = self.board.parse_san(move)  # Convert the move from SAN to a move object
            self.board.push(move_obj)  # Make the player's move on the board
            best_move_uci = self.get_best_move()  # Get the best move from the engine
            best_move_obj = chess.Move.from_uci(best_move_uci)  # Convert UCI move to move object
            best_move_san = self.board.san(best_move_obj)  # Convert move object to SAN format
            self.board.push(best_move_obj)  # Make the engine's move on the board
            return True, str(self.board), best_move_san
        except ValueError:  # Catch invalid moves
            return False, "Invalid move. Try again.", None

    # Retrieve the best move from the Stockfish engine based on the current board position
    def get_best_move(self):
        self.stockfish.set_fen_position(self.board.fen())  # Set the current board position in FEN format for Stockfish
        return self.stockfish.get_best_move()  # Get the best move from Stockfish

    # Check if the game is over
    def is_game_over(self):
        return self.board.is_game_over()

    # Determine the outcome of the game if it's over
    def game_outcome(self):
        if self.board.is_checkmate():
            winner = "Black" if self.board.turn else "White"  # Determine the winner
            return f"Checkmate! {winner} wins."
        elif self.board.is_stalemate():
            return "Stalemate! The game is a draw."
        elif self.board.is_insufficient_material():
            return "Draw due to insufficient material."
        elif self.board.is_game_over():
            return "Game over!"

    # Print the current state of the board
    def print_board(self):
        return str(self.board)