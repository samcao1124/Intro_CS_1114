"""
DEFINE YOUR FUNCTIONS BELOW
"""

"""
DEFINE YOUR FUNCTIONS ABOVE
"""


def main():
    """
    Just some sample behavior.
    """
    print_powers_of()


def print_powers_of():
    # print_even_powers_of_in_reverse()
    base = float(input("Please enter a positive integer to serve as the base"))
    power = float(input("Please enter a positive integer to serve as the highest power"))
    if base < 0 or base % 1 != 0:
        print("ERROR: Both values must be POSITIVE INTEGERS.")
    else:
        for i in range(0, int(power) + 1):
            print(int(base) ** i)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
