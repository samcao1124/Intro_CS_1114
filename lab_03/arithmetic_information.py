"""
WRITE YOUR FUNCTION DEFINITION BELOW
"""
def print_arithmetic_information():

    num_1= 10
    num_2= 4
    if  num_1 < 0 or num_2 <0:
        print("values must be positive")
    else:
        sum= num_1+num_2
        difference= num_1-num_2
        product= num_1*num_2
        quotient= num_1//num_2
        remainder= num_1%num_2
        print(str(sum) + "\n" + str(difference)+"\n"+str(product)+"\n"+str(quotient)+"\n"+str(remainder)+"\n")


"""
WRITE YOUR FUNCTION DEFINITION ABOVE
"""


def main():
    """
    Just some sample behavior.
    """
    print_arithmetic_information()

### DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
