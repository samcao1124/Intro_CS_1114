# Author: <Sam Cao>
# Assignment #3 - Blackjack
# Date due: 2021-03-25
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16


####### DO NOT EDIT ABOVE ########
def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple

    :return: a single- or double-character string representing a playing card

    >>> random.seed(13)
    >>> deal_card()
    '5'
    >>> deal_card()
    '5'
    >>> deal_card()
    'J'
    """
    card_in_hand = random.choice(CARD_LABELS)
    return (card_in_hand)
def get_card_value(card_label):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)

    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value

    >>> card_label = 'A'
    >>> get_card_value(card_label)
    1
    >>> card_label = 'K'
    >>> get_card_value(card_label)
    10
    >>> card_label = '5'
    >>> get_card_value(card_label)
    5
    """
    if card_label == "A":
        return 1
    elif card_label == "2":
        return 2
    elif card_label == "3":
        return 3
    elif card_label == "4":
        return 4
    elif card_label == "5":
        return 5
    elif card_label == "6":
        return 6
    elif card_label == "7":
        return 7
    elif card_label == "8":
        return 8
    elif card_label == "9":
        return 9
    elif card_label == "10":
        return 10
    elif card_label == "J":
        return 10
    elif card_label == "Q":
        return 10
    elif card_label == "K":
        return 10
def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total

    :return: the total value of the cards dealt
    """
    drew_1 = random.choice(CARD_LABELS)
    drew_2 = random.choice(CARD_LABELS)
    print("Player drew",str(drew_1),"and", drew_2 +".")
    total_value = get_card_value(drew_1) + get_card_value(drew_2)
    print("Player's total is",str(total_value)+".""\n")
    while total_value < BLACKJACK :
        player_choice = input("Hit (h) or Stay (s)?")
        print()
        if player_choice == "h":
            drew_3 = random.choice(CARD_LABELS)
            total_value += get_card_value(drew_3)
            print("Player drew",str(drew_3)+".")
            print("Player's total is",str(total_value)+".""\n")
        elif player_choice == "s":
            return total_value
    return total_value
def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total

    :return: the total value of the cards dealt
    """
    drew_num = 0
    drew_1 = deal_card()
    drew_2 = deal_card()
    print("The dealer has",str(drew_1),"and", drew_2 +".")
    total_value = get_card_value(drew_1) + get_card_value(drew_2)
    print("Dealer's total is",str(total_value)+".""\n")
    while int(total_value) <= DEALER_THRESHOLD :
        drew_num = random.choice(CARD_LABELS)
        total_value += get_card_value(drew_num)
        print("Dealer drew",str(drew_num)+".")
        print("Dealer's total is",str(total_value)+".""\n")
    return total_value
def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.

    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """

    if dealer_total < player_total <= BLACKJACK or player_total <= BLACKJACK < dealer_total:
        print("YOU WIN!"+"\n")
    else:
        print("YOU LOSE!"+"\n")


def play_blackjack():
    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome

    :return: None
    """
    print("Let's Play Blackjack!"+"\n")
    again = "Y"
    while again == "Y":
        player = deal_cards_to_player()
        if player <= BLACKJACK:
            deal = deal_cards_to_dealer()
        else:
            deal = 0
        determine_outcome(player, deal)
        again = input("Play again (Y/N)? ")
        print()
        while again != "N" and again != "Y":
            again = input("Play again (Y/N)? ")
            print()
    print("Goodbye.")








def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """
    play_blackjack()

    # call play_blackjack() here and remove pass below



####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    #Remove comments for next 4 lines to run doctests
    #print("Running doctests...")
    #import doctest
    #doctest.testmod(verbose=True)

    #print("\nRunning program...\n")

    main()
