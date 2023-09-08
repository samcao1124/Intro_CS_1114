def is_password_valid(test_password):
    val_up=0
    val_low=0
    val_num=0
    val_alp=0

    for char in test_password:
        if char.isupper():
            val_up = val_up+1

        if char.islower():
            val_low = val_low+1

        if char.isalnum():
            val_num=val_num+1

        if char.isalpha():
            val_alp=val_alp+1
    if val_up >= 2 and val_low >= 2 and val_alp >= 2 and val_num >= 1 and len(test_password) >= 8:
        return(True)
    else:
        return(False)










def main():
    """
    Just some sample behavior. Feel free to try your own!
    """
    test_password = "NAit1!"

    if is_password_valid(test_password):
        print("This is a valid password!")
    else:
        print("This is not a valid password!")

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
