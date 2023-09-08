from karel.stanfordkarel import *


def pave_all_hurdles():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """

    # YOU ARE FREE TO DIVIDE YOUR PROBLEM UP THIS WAY, BUT IF YOU PREFER ANY OTHER WAY, DO WHATEVER MAKES MOST SENSE
    # TO YOU!
    # THE FUNCTION pave_all_hurdles() IS THE ONLY FUNCTION THAT IS REQUIRED FOR THIS PROGRAM TO RUN.
    while front_is_clear():
        pave_hurdle()
        move_to_wall()
    put_beeper()



def pave_hurdle():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """

    while front_is_clear():
        put_beeper()
        move()
        if right_is_clear():
            turn_right()
            if not front_is_clear():
                turn_right()




def turn_right():
    turn_left()
    turn_left()
    turn_left()



def move_to_wall():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """

    if not front_is_clear():
        turn_left()


def move_with_wall_on_right():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """

    pass


def main():
    pave_all_hurdles()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
