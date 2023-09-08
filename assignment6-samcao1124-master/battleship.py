# Author: <Sam Cao>
# Assignment #6 - Battleship
# Date due: 2021-05-06
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import random
### DO NOT EDIT BELOW (with the exception of MAX_MISSES) ###

HIT_CHAR = 'x'
MISS_CHAR = 'o'
BLANK_CHAR = '.'
HORIZONTAL = 'h'
VERTICAL = 'v'
MAX_MISSES = 20
SHIP_SIZES = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
NUM_ROWS = 10
NUM_COLS = 10
ROW_IDX = 0
COL_IDX = 1
MIN_ROW_LABEL = 'A'
MAX_ROW_LABEL = 'J'


def get_random_position():
    """Generates a random location on a board of NUM_ROWS x NUM_COLS."""

    row_choice = chr(
                    random.choice(
                        range(
                            ord(MIN_ROW_LABEL),
                            ord(MIN_ROW_LABEL) + NUM_ROWS
                        )
                    )
    )

    col_choice = random.randint(0, NUM_COLS - 1)

    return (row_choice, col_choice)


def play_battleship():
    """Controls flow of Battleship games including display of
    welcome and goodbye messages.

    :return: None
    """

    print("Let's Play Battleship!\n")

    game_over = False

    while not game_over:

        game = Game()
        game.display_board()

        while not game.is_complete():
            pos = game.get_guess()
            result = game.check_guess(pos)
            game.update_game(result, pos)
            game.display_board()

        game_over = end_program()

    print("Goodbye.")

### DO NOT EDIT ABOVE (with the exception of MAX_MISSES) ###


class Ship:
    def __init__(self, name, start_position, orientation):
        """Creates a new ship with the given name, placed at start_position in the
        provided orientation. The number of positions occupied by the ship is determined
        by looking up the name in the SHIP_SIZE dictionary.

        :param name: the name of the ship
        :param start_position: tuple representing the starting position of ship on the board
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return: None
        """
        self.name = name
        self.start_position = start_position
        self.orientation = orientation
        self.positions = {}
        self.sunk = False
        if orientation == VERTICAL:
            for steps in range(SHIP_SIZES[name]):
                position = (chr(ord(start_position[ROW_IDX]) + steps) ,start_position[COL_IDX])
                self.positions[position] = self.sunk
        elif orientation == HORIZONTAL:
            for steps in range(SHIP_SIZES[name]):
                position = (start_position[ROW_IDX] ,start_position[COL_IDX] + steps)
                self.positions[position] = self.sunk


class Game:
    def __init__(self, max_misses = MAX_MISSES):
        """" Creates a new game with max_misses possible missed guesses.
        The board is initialized in this function and ships are randomly
        placed on the board.

        :param max_misses: maximum number of misses allowed before game ends
        """
        self.max_misses = max_misses
        self.board = {}
        self.guesses = []
        self.ships = []
        self.initialize_board()
        self.create_and_place_ships()




    def initialize_board(self):
        """Sets the board to it's initial state with each position occupied by
        a period ('.') string.

        :return: None
        """
        for char in range(ord(MIN_ROW_LABEL),ord(MAX_ROW_LABEL) + 1):
            self.board[chr(char)] = [BLANK_CHAR] * NUM_COLS



    ########## DO NOT EDIT #########
    
    _ship_types = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    
    
    def display_board(self):
        """ Displays the current state of the board."""

        print()
        print("  " + ' '.join('{}'.format(i) for i in range(len(self.board))))
        for row_label in self.board.keys():
            print('{} '.format(row_label) + ' '.join(self.board[row_label]))
        print()

    ########## DO NOT EDIT #########



    def in_bounds(self, start_position, ship_size, orientation):
        """Checks that a ship requiring ship_size positions can be placed at start position.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement inside board boundary, False otherwise
        """

        if orientation == VERTICAL:
            for steps in range(ship_size):
                position = (chr(ord(start_position[ROW_IDX]) + steps) ,start_position[COL_IDX])
                if ord(position[ROW_IDX]) > ord(MAX_ROW_LABEL):
                    return False
        elif orientation == HORIZONTAL:
            for steps in range(ship_size):
                position = (start_position[ROW_IDX] ,start_position[COL_IDX] + steps)
                if position[COL_IDX] >= NUM_COLS:
                    return False
        return True

    def overlaps_ship(self, start_position, ship_size, orientation):
        """Checks for overlap between previously placed ships and a potential new ship
        placement requiring ship_size positions beginning at start_position in the
        given orientation.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement overlaps previously placed ship, False otherwise
        """

        if orientation == VERTICAL:
            for steps in range(ship_size):
                new_position = (chr(ord(start_position[ROW_IDX]) + steps) ,start_position[COL_IDX])
                for ship in self.ships:
                    if new_position in ship.positions:
                        return True
        elif orientation == HORIZONTAL:
            for steps in range(ship_size):
                new_position = (start_position[ROW_IDX] ,start_position[COL_IDX] + steps)
                for ship in self.ships:
                    if new_position in ship.positions:
                        return True
        return False



    def place_ship(self, start_position, ship_size):
        """Determines if placement is possible for ship requiring ship_size positions placed at
        start_position. Returns the orientation where placement is possible or None if no placement
        in either orientation is possible.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :return orientation: 'h' if horizontal placement possible, 'v' if vertical placement possible,
            None if no placement possible
        """
        if self.in_bounds(start_position,ship_size,orientation = HORIZONTAL) == True and self.overlaps_ship(start_position,ship_size,orientation = HORIZONTAL) == False:
            return HORIZONTAL
        elif self.in_bounds(start_position,ship_size,orientation = VERTICAL) == True and self.overlaps_ship(start_position,ship_size,orientation = VERTICAL) == False:
            return VERTICAL
        else:
            return None


    def create_and_place_ships(self):
        """Instantiates ship objects with valid board placements.

        :return: None
        """
        for ships in self._ship_types:
            new_orientation = None
            while new_orientation != HORIZONTAL and new_orientation != VERTICAL:
                random_position = get_random_position()
                sizes = SHIP_SIZES[ships]
                new_orientation = self.place_ship(random_position,sizes)
            new_ship = Ship(ships,random_position,new_orientation)
            self.ships.append(new_ship)


    def get_guess(self):
        """Prompts the user for a row and column to attack. The
        return value is a board position in (row, column) format

        :return position: a board position as a (row, column) tuple
        """

        row = input("Enter a row: ")
        while not MIN_ROW_LABEL <= row <= MAX_ROW_LABEL:
            row = input("Enter a row: ")
        column = input("Enter a column: ")
        while not ROW_IDX <= int(column) < NUM_COLS:
            column = input("Enter a column: ")
        position = (row, int(column))
        return position

    def check_guess(self, position):
        """Checks whether or not position is occupied by a ship. A hit is
        registered when position occupied by a ship and position not hit
        previously. A miss occurs otherwise.

        :param position: a (row,column) tuple guessed by user
        :return: guess_status: True when guess results in hit, False when guess results in miss
        """

        for ship in self.ships:
            if position in ship.positions and ship.positions[position] == False:
                ship.positions[position] = True
                sunk_amount = 0
                for single_position in ship.positions:
                    if ship.positions[single_position] == True:
                        sunk_amount += 1
                ship_size = len(ship.positions.keys())
                if ship_size == sunk_amount:
                    print("You sunk the {}!".format(ship.name))
                    ship.sunk = True
                return True
        return False


    def update_game(self, guess_status, position):
        """Updates the game by modifying the board with a hit or miss
        symbol based on guess_status of position.

        :param guess_status: True when position is a hit, False otherwise
        :param position:  a (row,column) tuple guessed by user
        :return: None
        """

        if guess_status:
            self.board[position[ROW_IDX]][position[COL_IDX]] = HIT_CHAR

        else:
            if self.board[position[ROW_IDX]][position[COL_IDX]] != HIT_CHAR:
                self.board[position[ROW_IDX]][position[COL_IDX]] = MISS_CHAR
            self.guesses.append(position)



    def is_complete(self):
        """Checks to see if a Battleship game has ended. Returns True when the game is complete
        with a message indicating whether the game ended due to successfully sinking all ships
        or reaching the maximum number of guesses. Returns False when the game is not
        complete.

        :return: True on game completion, False otherwise
        """
        if len(self.guesses) == MAX_MISSES:
            print("SORRY! NO GUESSES LEFT.")
            return True
        for ship in self.ships:
            if ship.sunk == False:
                return False
        print("YOU WIN!")
        return True




def end_program():
    """Prompts the user with "Play again (Y/N)?" The question is repeated
    until the user enters a valid response (Y/y/N/n). The function returns
    False if the user enters 'Y' or 'y' and returns True if the user enters
    'N' or 'n'.

    :return response: boolean indicating whether to end the program
    """
    finish = False
    while not finish:
        response = input("Play again (Y/N)?")
        if response == "Y" or response == "y":
            return False
        elif response == "N" or response == "n":
            return True






def main():
    """Executes one or more games of Battleship."""

    play_battleship()


if __name__ == "__main__":
    main()
