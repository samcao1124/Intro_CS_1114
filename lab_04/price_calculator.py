"""
DEFINE YOUR FUNCTIONS BELOW
"""



"""
DEFINE YOUR FUNCTIONS ABOVE
"""
def get_final_price():
    final_price = int(input("Enter the price of your item:"))
    num_item = 1
    while final_price <1000:
        final_price += int(input("Enter the price of your item:"))
        num_item += 1
    final_price = final_price*(1+0.08)
    if num_item > 10:
        final_price = final_price*(1-0.2)
        print("20% Discount applied!")
    else:
        print("The total price is $",final_price)
    print("The total price is $",final_price)














def main():
    """
    Just some sample behavior.
    """
    get_final_price()

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
