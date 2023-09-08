from karel.stanfordkarel import *


def main():
    infinite_loop()


def infinite_loop():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """

    while front_is_clear():
        move()
    if left_is_clear():
        turn_left()
    while front_is_clear():
        move()
        if not front_is_clear():
            turn_left()






def turn_right():
    turn_left()
    turn_left()
    turn_left()




####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
