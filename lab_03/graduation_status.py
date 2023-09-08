def print_graduation_status():
    """
    Given a series of hard-coded values for dean permission, advisor permission, approved senior status, and amount of
    accumulated credits, prints whether or not a student can graduate.

    :return: None.
    """
    # Student information
    has_dean_permission = False
    has_advisor_permission = True
    is_approved_senior = False
    accumulated_credits = 50

    # Graduation status display; this is what the students will start with.
    if accumulated_credits > 40 and has_advisor_permission:
        print("This student can graduate.")
    elif accumulated_credits > 60 and is_approved_senior:
        print("This student can graduate.")
    elif has_dean_permission and accumulated_credits > 64:
        print("This student can graduate.")
    else:
        print("This student cannot graduate.")


def main():
    print_graduation_status()


### DO NOT WRITE CODE BELOW THIS LINE.


if __name__ == '__main__':
    main()
