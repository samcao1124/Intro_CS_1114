def get_gamma(side_a, side_b, side_c):
    import math
    c = side_c
    b = side_b
    a = side_a
    if a + b > c or a + c > b or b + c > a:
        gamma = math.acos((c**2 - a**2 - b**2) / (- 2 * a * b))
        gamma_degree = math.degrees(gamma)
        return gamma_degree
    else:
        return (-1)
    if a < 0 or b < 0 or c < 0:
        return (-1)



def main():
    """
    Just an example. Feel free to try your own, but note that the auto-grader will only be evaluating the function
    get_gamma() and will completely ignore the main function!
    """

    side_1 = 7
    side_2 = 10
    side_3 = 5

    gamma = get_gamma(side_1, side_2, side_3)

    if gamma != -1:
        print("Side lengths {}, {}, and {} yield a {} value for angle gamma.".format(side_1, side_2, side_3, gamma))
    else:
        print("Side lengths {}, {}, and {} are invalid.".format(side_1, side_2, side_3))


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
