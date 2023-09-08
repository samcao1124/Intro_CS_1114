from karel.stanfordkarel import *


def main():
    pick_up_top_beepers()


def pick_up_top_beepers():

    while front_is_clear():
        move()

    if left_is_clear():
            turn_left()
    while front_is_clear():
        move()

    if left_is_clear():
        turn_left()
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
    if left_is_clear():
        turn_left()
        while front_is_clear():
            move()
    if left_is_clear():
        turn_left()



####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
