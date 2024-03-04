from art import *

# Set up the game board
col_names = ["A", "B", "C"]
row_names = ["1", "2", "3"]
game_squares = [[c + r for r in row_names] for c in col_names]
available_squares = game_squares[0] + game_squares[1] + game_squares[2]

rows_list = [[available_squares[0], available_squares[3], available_squares[6]],
             [available_squares[1], available_squares[4], available_squares[7]],
             [available_squares[2], available_squares[5], available_squares[8]]]

cols_list = [[available_squares[0], available_squares[1], available_squares[2]],
             [available_squares[3], available_squares[4], available_squares[5]],
             [available_squares[6], available_squares[7], available_squares[8]]]

diags_list = [[available_squares[0], available_squares[4], available_squares[8]],
              [available_squares[2], available_squares[4], available_squares[6]]]

# print(rows_list)
# print(cols_list)
# print(diags_list)

game_dict = {item: " " for item in available_squares}

tic_dict = {"p1": "X", "p2": "0"}

# Set the initial conditions
valid_choice = False
square: str
current_player = "p1"
game_over = False
win = False
draw = False
play_again = False


# Game functionality
def validate_choice(sq):
    if sq in game_dict.keys():
        # Player selected a valid square and it is blank
        if game_dict[sq] == " ":
            global valid_choice
            valid_choice = True
        # Player selected a valid square and it is not blank
        else:
            print("That space is already taken. Please make a valid selection.")
            # # Restart the selection function
            # player_selection(current_player)
    else:
        # Player did not select a valid square
        print("That is not a valid square. Please make a valid selection.")
        # # Restart the selection function
        # player_selection(current_player)


def player_selection(pl):
    print("Here is a reference board to make your selection:")
    print(reference_board)

    if pl == "p1":
        p1_square = input("It's your turn Player 1. Please make your selection: ").upper()
        validate_choice(p1_square)
        return p1_square
    elif pl == "p2":
        p2_square = input("It's your turn Player 2. Please make your selection: ").upper()
        validate_choice(p2_square)
        return p2_square


def new_game():
    print("Welcome to TicTac Toe!")
    print("Player 1 is X. Player 2 is 0.")


def print_current_board(dt):
    print(f"""
     {dt['A1']} | {dt['B1']} | {dt['C1']}
    -----------
     {dt['A2']} | {dt['B2']} | {dt['C2']}
    -----------
     {dt['A3']} | {dt['B3']} | {dt['C3']}
    """)


def check_endgame(dt, pl):
    global draw
    global win
    draw = False
    mark = tic_dict[pl]
    row_win = False
    col_win = False
    diag_win = False

    # Check draw
    draw_res = all(x != " " for x in game_dict.values())
    if draw_res:
        draw = True
        return draw

    # Check win
    else:

        # Check 3 in a row
        for r in range(len(rows_list)):
            row_dict = {k: v for k, v in dt.items() if k in rows_list[r]}
            # print(row_dict)
            row_res = all(x == mark for x in row_dict.values())
            # print(row_res)
            if row_res:
                row_win = True

        # Check 3 in a column
        for c in range(len(cols_list)):
            col_dict = {k: v for k, v in dt.items() if k in cols_list[c]}
            # print(col_dict)
            col_res = all(x == mark for x in col_dict.values())
            # print(col_res)
            if col_res:
                col_win = True

        # Check for 3 on a diagonal
        for d in range(len(diags_list)):
            diags_dict = {k: v for k, v in dt.items() if k in diags_list[d]}
            # print(diags_dict)
            diag_res = all(x == mark for x in diags_dict.values())
            # print(diag_res)
            if diag_res:
                diag_win = True

        if row_win or col_win or diag_win:
            win = True
        else:
            win = False

        return win


# Run the game
new_game()

while not game_over:
    while not valid_choice:
        square = player_selection(current_player)

    while valid_choice:
        # Update board
        game_dict[square] = tic_dict[current_player]
        # Show the board
        print_current_board(game_dict)
        # Check win conditions
        game_over = check_endgame(game_dict, current_player)
        # Reset while loop
        valid_choice = False

    if game_over:
        if win:
            print(f"{tic_dict[current_player]}'s won! Congratulations")
        elif draw:
            print("It's a draw - Better luck next time!")
        # Reset the game
        another_game = input("Would you like to play again? Y/N ")
        if another_game == "Y":
            game_over = False
            game_dict = {item: " " for item in available_squares}

    else:
        # Pass the turn to the next player
        if current_player == "p1":
            current_player = "p2"
        else:
            current_player = "p1"

