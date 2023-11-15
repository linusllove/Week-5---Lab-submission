# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player

# Reminder to check all the tests

# cli.py

from logic import make_empty_board, get_winner, other_player, HumanPlayer, BotPlayer

def print_board(board):
    for row in board:
        print(" | ".join(cell if cell is not None else " " for cell in row))
        print("---------")

def play_game(player1, player2):
    board = make_empty_board()
    winner = None
    current_player = player1

    while winner is None:
        print_board(board)
        print(f"Player {current_player.marker}'s turn")

        move = current_player.make_move(board)

        if move:
            row, col = move
            board[row][col] = current_player.marker
            winner = get_winner(board)
            current_player = player2 if current_player == player1 else player1  # Switch player

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

if __name__ == '__main__':
    # Example: Single player vs Bot
    player1 = HumanPlayer('X')
    player2 = BotPlayer('O')
    play_game(player1, player2)






