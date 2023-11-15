# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

# logic.py

class Player:
    def __init__(self, marker):
        self.marker = marker

    def make_move(self, board):
        raise NotImplementedError("Subclasses must implement this method")

class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if board[row][col] is None:
                    return row, col
                else:
                    print("That cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column values.")

class BotPlayer(Player):
    def make_move(self, board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        return empty_cells[0] if empty_cells else None

