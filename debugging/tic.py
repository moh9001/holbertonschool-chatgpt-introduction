#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid coordinates. Please choose 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

