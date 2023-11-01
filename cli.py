# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player

# Reminder to check all the tests

def print_board(board):
    for row in board:
        print(" | ".join(cell if cell is not None else " " for cell in row))
        print("---------")


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'
    
    while winner == None:
        print_board(board)
        print(f"Player {current_player}'s turn")

        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if board[row][col] is None:
                    break
                else:
                    print("That cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column values.")

        board[row][col] = current_player
        winner = get_winner(board)
        current_player = other_player(current_player)

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

