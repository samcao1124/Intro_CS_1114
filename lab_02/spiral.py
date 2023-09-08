from karel.stanfordkarel import *


def main():
    spiral()


def spiral():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """

    # YOU ARE FREE TO DIVIDE YOUR PROBLEM UP THIS WAY, BUT IF YOU PREFER ANY OTHER WAY, DO WHATEVER MAKES MOST SENSE
    # TO YOU!
    # THE FUNCTION spiral() IS THE ONLY FUNCTION THAT IS REQUIRED FOR THIS PROGRAM TO RUN.
    reach_center()
    turn_around()
    leave_spiral()


def reach_center():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """
    pass


def leave_spiral():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """
    pass


def turn_around():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """
    pass


def turn_right():
    """
    Instructs Karel to perform a right turn.

    pre-condition:  Karel is be facing any of the four cardinal directions.
    post-condition: Karel will have performed a 45-degree turn in the RIGHT direction.
    """

    turn_around()
    turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
