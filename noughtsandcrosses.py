import random
import os.path
import json
import os

random.seed(1)

def draw_board(board):

    """
    Prints the game board to the console using ANSI escape sequences for formatting.

    Args:
       board (list): A 3x3 list representing the game board, where each element is ' ', 'X', or 'O'.
    """
    
    for i in range(3): #for each row
        print("\033[91m-------------\033[0m")
        for j in range(3): #for each column
            print("\033[91m|\033[0m", board[i][j], end=" ")
        print("\033[91m|\033[0m")
    print("\033[91m-------------\033[0m")
    

def welcome(board):
    """
    Prints a welcome message to the console and displays the initial game board.

    Args:
        board (list): A 3x3 list representing the game board, where each element is ' ', 'X', or 'O'.
    """
    
    print("\033[91mWelcome to 'Unbeatable Noughts and Crosses!' \033[0m")
    draw_board(board)

def initialise_board(board):

    """
    Initializes the game board with all empty cells (' ').

    Args:
        board (list): A 3x3 list representing the game board, where each element is ' ', 'X', or 'O'.

    Returns:
        list: The initialized game board with all empty cells.
    """
    
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board
    
def get_player_move(board):
            
            """
    Gets the player's move by prompting for a valid cell position (1-9).

    Args:
        board (list): A 3x3 list representing the game board, where each element is ' ', 'X', or 'O'.

    Returns:
        tuple: A tuple (row, col) representing the chosen cell position.
    """
    
            while True:
                try:
                    position = int(input(""" 
                                      1 2 3
                                      4 5 6                    
Enter the position of the cell (1-9): 7 8 9  : """))

                    if position < 1 or position > 9:
                        print("Out of range! Enter a number corresponding to the cell position.")
                        continue

                    row = (position - 1) // 3
                    col = (position - 1) % 3

                    if board[row][col] != ' ':
                        print("Cell already occupied. Please choose another position.")
                        continue

                    return row, col
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")
                

def choose_computer_move(board):

    """
    Selects a random empty cell as the computer's move.

    Args:
        board (list): A 3x3 list representing the game board, where each element is ' ', 'X', or 'O'.

    Returns:
        tuple: A tuple (row, col) representing the chosen cell position for the computer.
    """
    
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    row, col = random.choice(empty_cells)
    return row, col


def check_for_win(board, mark):

    """
    Checks if the given mark ('X' or 'O') has achieved a winning condition on the board.

    Args:
        board (list): A 3x3 list representing the game board, where each element is ' ', 'X', or 'O'.
        mark (str): The mark to check for a win ('X' or 'O').

    Returns:
        bool: True if the mark has won, False otherwise.
    """
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

def check_for_draw(board):

    """
    Checks if the game has ended in a draw (no empty cells remaining).

    Args:
        board (list): A 3x3 list representing the game board, where each element is ' ', 'X', or 'O'.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
  
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True
        
def play_game(board):

    """
    Main function that manages the entire game loop, including player moves,
    computer moves, and checking for win/draw conditions.

    Args:
        board (list): A 3x3 list representing the game board, where each element is ' ', 'X', or 'O'.

    Returns:
        int: 1 if player wins, -1 if computer wins, 0 if draw.
    """
    
    board = initialise_board(board)
    draw_board(board)
    
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        
        if check_for_win(board, 'X'):
            return 1
        
        if check_for_draw(board):
            return 0
        
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        
        if check_for_win(board, 'O'):
            return -1
        
        if check_for_draw(board):
            return 0
                    
                
def menu():
    """
    Displays the game menu and prompts the user for their choice.

    Returns:
        str: The user's choice (1, 2, 3, or 'q').
    """
  
    choice = input("""Enter your choice (1, 2, 3, or q):
    1 - Play the game
    2 - Save score in file 'leaderboard.txt'
    3 - Load and display the scores from the 'leaderboard.txt'
    q - End the program \n 1, 2, 3 or q ? :""")
    return choice

def load_scores():

    """
    Loads the leaderboard data from the 'leaderboard.txt' file, if it exists.

    Returns:
        dict: A dictionary containing the leaderboard data, where keys are names and values are scores.
    """
  
    if os.path.exists('leaderboard.txt') and os.path.getsize('leaderboard.txt') > 0:
        with open('leaderboard.txt', 'r') as file:
            leaders = json.load(file)
    else:
        leaders = {}
    return leaders
    
def save_score(score):

    """
    Saves the player's score to the 'leaderboard.txt' file, along with their name.

    Args:
        score (int): The player's score (1 for win, 0 for draw, -1 for loss).
    """
   
    name = input("Enter your name: ")
    while not name:
        name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)

def display_leaderboard(leaders):

    """
    Presents the leaderboard information to the user in a clear and informative way.

    Args:
        leaders (dict): A dictionary containing leaderboard entries where keys are names and values are scores.

        Prints proper message when the leaderboard dictionary is empty.
    """
  
    if not leaders:
        print("No records in leaderboard.\nPlay the game to add your score.")
    else:
        for name, score in leaders.items():
            print(f"{name}: {score}")
