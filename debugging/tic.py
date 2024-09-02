#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.
    
    Parameters:
    board (list of list): 2D list representing the game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.
    
    Parameters:
    board (list of list): 2D list representing the game board.
    
    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Checks if the game is a draw.
    
    Parameters:
    board (list of list): 2D list representing the game board.
    
    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # Check if input is within the valid range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            # Check if the cell is empty
            if board[row][col] == " ":
                board[row][col] = player
            else:
                print("That spot is already taken! Try again.")
                continue

            # Check if there is a winner
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
            
            # Check if the game is a draw
            if check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break

            # Switch player
            player = "O" if player == "X" else "X"
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        except IndexError:
            print("Invalid input. Please enter numbers between 0 and 2.")
        
if __name__ == "__main__":
    tic_tac_toe()

