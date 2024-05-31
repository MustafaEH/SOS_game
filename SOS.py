# Initialize the game board with cell identifiers
board = [["0,0", "0,1", "0,2", "0,3", "0,4"],
         ["1,0", "1,1", "1,2", "1,3", "1,4"],
         ["2,0", "2,1", "2,2", "2,3", "2,4"],
         ["3,0", "3,1", "3,2", "3,3", "3,4"],
         ["4,0", "4,1", "4,2", "4,3", "4,4"]]

# Function to display the current state of the board
def display_board():
    for row in board:
        print(" | ".join(row))  # Join elements with ' | ' for better readability
    print("\n")  # Add a newline for better separation between board displays

# List of valid game letters
game_letter = ["S", "O"]

# Global variables for player scores
player1_score = 0
player2_score = 0

# Function to handle a player's turn
def game_process_player(player):
    global player1_score, player2_score  # Refer to the global score variables

    print(f"Player {player} turn.")  # Indicate which player's turn it is
    x = input("Enter no. of row: ").strip()  # Get row number from the player
    y = input("Enter no. of column: ").strip()  # Get column number from the player
    letter = input("Choose letter (S or O): ").strip().upper()  # Get and convert the letter to uppercase

    # Validate the row and column input
    while not x.isdigit() or not y.isdigit() or int(x) > 4 or int(x) < 0 or int(y) > 4 or int(y) < 0:
        print("Please choose valid numbers (0-4).")
        x = input("Enter no. of row: ").strip()
        y = input("Enter no. of column: ").strip()
    x, y = int(x), int(y)

    # Validate the letter input
    while letter not in game_letter:
        print("Just S or O!")
        letter = input("Choose letter (S or O): ").strip().upper()

    avilable_cell(x, y)  # Check if the cell is available
    board[x][y] = " " + letter + " "  # Place the letter on the board

    # Calculate points based on the letter placed
    if letter == "S":
        points = get_points_S(x, y)
    elif letter == "O":
        points = get_points_O(x, y)

    # Update the player's score
    if player == 1:
        player1_score += points
    else:
        player2_score += points

    print(f"Player 1 score: {player1_score}")
    print(f"Player 2 score: {player2_score}")

    return points  # Return the points scored by the player in this turn

# Function to calculate points for 'S' placement
def get_points_S(i, j):
    points = 0
    # Check various possible 'SOS' patterns
    if j + 2 <= 4 and board[i][j:j + 3] == [" S ", " O ", " S "]:
        points += 1
    if j - 2 >= 0 and board[i][j - 2:j + 1] == [" S ", " O ", " S "]:
        points += 1
    if i + 2 <= 4 and [board[i][j], board[i + 1][j], board[i + 2][j]] == [" S ", " O ", " S "]:
        points += 1
    if i - 2 >= 0 and [board[i][j], board[i - 1][j], board[i - 2][j]] == [" S ", " O ", " S "]:
        points += 1
    if i + 2 <= 4 and j + 2 <= 4 and [board[i][j], board[i + 1][j + 1], board[i + 2][j + 2]] == [" S ", " O ", " S "]:
        points += 1
    if i - 2 >= 0 and j - 2 >= 0 and [board[i][j], board[i - 1][j - 1], board[i - 2][j - 2]] == [" S ", " O ", " S "]:
        points += 1
    if i - 2 >= 0 and j + 2 <= 4 and [board[i][j], board[i - 1][j + 1], board[i - 2][j + 2]] == [" S ", " O ", " S "]:
        points += 1
    if i + 2 <= 4 and j - 2 >= 0 and [board[i][j], board[i + 1][j - 1], board[i + 2][j - 2]] == [" S ", " O ", " S "]:
        points += 1

    return points

# Function to calculate points for 'O' placement
def get_points_O(i, j):
    points = 0
    # Check various possible 'SOS' patterns involving 'O'
    if j > 0 and j < 4 and board[i][j - 1:j + 2] == [' S ', ' O ', ' S ']:
        points += 1
    if i > 0 and i < 4 and [board[i - 1][j], board[i][j], board[i + 1][j]] == [' S ', ' O ', ' S ']:
        points += 1
    if i > 0 and i < 4 and j > 0 and j < 4:
        if [board[i + 1][j + 1], board[i][j], board[i - 1][j - 1]] == [' S ', ' O ', ' S ']:
            points += 1
        if [board[i - 1][j + 1], board[i][j], board[i + 1][j - 1]] == [' S ', ' O ', ' S ']:
            points += 1

    return points

# Function to check if the chosen cell is available
def avilable_cell(row, column):
    while board[row][column] in [" S ", " O "]:
        print("Unavailable cell.")
        row = int(input("Enter no. of row: ").strip())
        column = int(input("Enter no. of column: ").strip())

# Main game loop
while True:
    display_board()  # Display the board before each player's turn
    while True:  # Loop to handle Player 1's turn and potential extra turns
        points = game_process_player(1)
        display_board()
        if points == 0:  # If no points are scored, break out of the loop
            break
    while True:  # Loop to handle Player 2's turn and potential extra turns
        points = game_process_player(2)
        display_board()
        if points == 0:  # If no points are scored, break out of the loop
            break
