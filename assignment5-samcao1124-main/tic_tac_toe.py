# Author: <Sam Cao>
# Assignment #5 - Tic-tac-toe
# Date due: 2021-04-22
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT CODE BELOW ########

MAX_ROUNDS = 9
NUM_ROWS = 3
NUM_COLS = 3
NUM_POSITIONS = 9
ROW_POS = 0
COL_POS = 1

def reset_board(board):
    """Resets the board dict to its original state with each
    position being empty (i.e. the (row, column) key has a
    space character (' ') value).

    :param board: a dict of (row, column) tuple keys and string values
    :return: None

    >>> board = {(0, 0): 'X', (0, 1): ' ', (0, 2): ' ', (1, 0): 'O', (1, 1): ' ', (1, 2): 'O', (2, 0): 'X', (2, 1): ' ', (2, 2): ' '}
    >>> reset_board(board)
    >>> board
    {(0, 0): ' ', (0, 1): ' ', (0, 2): ' ', (1, 0): ' ', (1, 1): ' ', (1, 2): ' ', (2, 0): ' ', (2, 1): ' ', (2, 2): ' '}
    """
    reset = " "
    for x,y in board.items():
        y = " "
        board[x] = y
def get_current_player(round):
    """Returns the mark of the player whose turn it is in the current
    round of the game.

    :param round: integer value representing the round
    :return: 'X' or 'O' depending on round

    >>> round =  3
    >>> get_current_player(round)
    'O'
    >>> round = 8
    >>> get_current_player(round)
    'X'
    """
    if round % 2 == 0:
        return 'X'
    elif round % 2 != 0:
        return 'O'

def get_position_choice(board, player_mark):
    """Prompts the user for a valid (row, col) board position. Prompts
    for row and column are repeated until valid position provided. The
    valid (row, col) position chosen is returned.

    :param board: a dict of (row, col) tuple keys and string values
    :param player_mark: 'X' or 'O' depending on round
    :return: (row, col) tuple of integers representing valid position choice
    """

    print(player_mark + ",")
    found = False
    while not found:
        row, col = -1, -1
        while not ( row > -1 and row < NUM_ROWS):
            row = int(input("Choose your row: "))
        while not ( col > -1 and col < NUM_COLS):
            col = int(input("Choose your column: "))
        print(" ")
        if board[(row,col)] == " ":
            return (row,col)


def update_board(board, player_mark, position):
    """Updates the value at the key represented by position
    in board dictionary to player_mark.

    :param board: a dict of (row, col) tuple keys and string values
    :param player_mark: 'X' or 'O' depending on round
    :param position: (row, col) tuple representing position
    :return: None
    """
    board[position] = player_mark

def display_outcome(round):
    """Displays an outcome message for a completed Tic-tac-toe game.

    :param round: the final value of the round variable for the game
    :return: None

    >>> round = MAX_ROUNDS
    >>> display_outcome(round)
    It's a draw!
    <BLANKLINE>
    >>> round = 6
    >>> display_outcome(round)
    X wins!
    <BLANKLINE>
    >>> round = 5
    >>> display_outcome(round)
    O wins!
    <BLANKLINE>
    """
    if round == MAX_ROUNDS:
        print("It's a draw!"+"\n")
    elif round < MAX_ROUNDS and round % 2 == 0:
        print("X wins!"+"\n")
    elif round < MAX_ROUNDS and round % 2 != 0:
        print("O wins!"+"\n")

def check_positions(pos1_value, pos2_value, pos3_value):
    """Returns True when all parameters have a value of 'X' or
    all parameters have a value of 'O'. Returns False for all
    other value combinations.

    :param pos1_value: the first of 3 consecutive board position values
    :param pos2_value: the second of 3 consecutive board position values
    :param pos3_value: the third of 3 consecutive board position values
    :return: True when all 3 values are 'X' or when all 3 values are 'O', False otherwise

    >>> (pos_val1, pos_va2, pos_val3)  = ('X', 'X', 'X')
    >>> check_positions(pos_val1, pos_va2, pos_val3)
    True
    >>> (pos_val1, pos_val2, pos_val3)  = ('O', 'O', 'O')
    >>> check_positions(pos_val1, pos_val2, pos_val3)
    True
    >>> (pos_val1, pos_val2, pos_val3)  = (' ', ' ', ' ')
    >>> check_positions(pos_val1, pos_val2, pos_val3)
    False
    >>> (pos_val1, pos_val2, pos_val3)  = ('O', 'X', 'O')
    >>> check_positions(pos_val1, pos_val2, pos_val3)
    False
    >>> (pos_val1, pos_val2, pos_val3)  = ('X', 'X', ' ')
    >>> check_positions(pos_val1, pos_val2, pos_val3)
    False
    """
    if (pos1_value, pos2_value, pos3_value) == ('X', 'X', 'X') or (pos1_value, pos2_value, pos3_value) == ('O', 'O', 'O')  :
        return True
    else:
        return False

def is_game_complete(board):
    """Determines whether or not a winning configuration has been achieved in the game
    represented by the board. Returns True when a winning configuration is detected and
    False when no winning configuration exists on the board.

    :param board: a dict of (row, col) tuple keys and string values
    :return: True when a winning configuration is detected, False otherwise

    >>> board = {(0, 0): ' ', (0, 1): ' ', (0, 2): ' ', (1, 0): ' ', (1, 1): 'X', (1, 2): ' ', (2, 0): ' ', (2, 1): ' ', (2, 2): ' '}
    >>> is_game_complete(board)
    False
    >>> board = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'O', (1, 0): 'O', (1, 1): 'O', (1, 2): 'X', (2, 0): 'X', (2, 1): 'X', (2, 2): 'O'}
    >>> is_game_complete(board)
    False
    >>> board = {(0, 0): ' ', (0, 1): 'O', (0, 2): ' ', (1, 0): ' ', (1, 1): 'O', (1, 2): ' ', (2, 0): 'X', (2, 1): 'X', (2, 2): 'X'}
    >>> is_game_complete(board)
    True
    >>> board = {(0, 0): 'O', (0, 1): ' ', (0, 2): 'X', (1, 0): 'X', (1, 1): 'O', (1, 2): 'X', (2, 0): ' ', (2, 1): ' ', (2, 2): 'O'}
    >>> is_game_complete(board)
    True
    """
    if check_positions(board[(0,0)],board[(0,1)],board[(0,2)]):
        return True
    elif check_positions(board[(0,0)],board[(1,1)],board[(2,2)]):
        return True
    elif check_positions(board[(0,2)],board[(1,1)],board[(2,0)]):
        return True
    elif check_positions(board[(2,0)],board[(2,1)],board[(2,2)]):
        return True
    elif check_positions(board[(1,0)],board[(1,1)],board[(1,2)]):
        return True
    elif check_positions(board[(0,1)],board[(1,1)],board[(2,1)]):
        return True
    elif check_positions(board[(0,0)],board[(1,0)],board[(2,0)]):
        return True
    elif check_positions(board[(0,2)],board[(1,2)],board[(2,2)]):
        return True
    else:
        return False

def play_tic_tac_toe(board):
    """Controls Tic-tac-toe games. This includes prompting player's for
    position choices, checking for winning game configurations, and outputting
    the outcome of a game.

    :param board: a dict of (row, col) tuple keys and string values
    :return: None
    """
    round = 0
    finish = False
    print("Let's Play Tic-tac-toe!"+"\n")
    while not finish and round < MAX_ROUNDS:
        display_board(board)
        player = get_current_player(round)
        position = get_position_choice(board,player)
        update_board(board,player,position)
        finish = is_game_complete(board)
        if not finish:
            round += 1
    display_board(board)
    display_outcome(round)
    response = is_program_finished()
    while response == False:
        reset_board(board)
        round = 0
        finish = False
        while not finish and round < MAX_ROUNDS:
            display_board(board)
            player = get_current_player(round)
            position = get_position_choice(board,player)
            update_board(board,player,position)
            finish = is_game_complete(board)
            if not finish:
                round += 1
        display_board(board)
        display_outcome(round)
        response = is_program_finished()


    print("Goodbye.")

def is_program_finished():
    """Prompts the user with the message "Play again (Y/N)?". The question is repeated
    until the user enters a valid response (one of Y/y/N/n). The function
    returns False if the user enters 'Y' or 'y' and returns True if the user
    enters 'N' or 'n'.

    :return response: boolean representing program completion status
    """
    finish = False
    while not finish:
        response = input("Play again (Y/N)?")
        if response == "Y" or response == "y":
            print(" ")
            return False
        elif response == "N" or response == "n":
            print(" ")
            return True









def display_board(board):
    """Displays the board's current state as a 3x3 grid"""

    print("     0 1 2 ")

    for row in range(0, NUM_ROWS):
        print("  {}  ".format(row), end="")
        for col in range(0, NUM_COLS):
            if col == 0:
                print(board[(row, col)], end="")
            else:
                print("|{}".format(board[(row, col)]), end="")

        print(" ")

        if row < NUM_ROWS - 1:
            print("    --+-+--")
    print()

####### DO NOT EDIT CODE ABOVE ########


def main():

    ########## DO NOT EDIT DICTIONARY INITIALIZATION BELOW #########

    board = {
        (0,0): ' ', (0,1): ' ', (0,2): ' ',
        (1,0): ' ', (1,1): ' ', (1,2): ' ',
        (2,0): ' ', (2,1): ' ', (2,2): ' '
    }
    play_tic_tac_toe(board)

    ########## DO NOT EDIT DICTIONARY INITIALIZATION ABOVE #########
    
    # call play_tic_tac_toe() with board as argument and remove pass below
    pass

if __name__ == '__main__':
    main()
