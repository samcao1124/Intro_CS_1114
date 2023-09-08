"""
DEFINE YOUR FUNCTIONS BELOW
"""



"""
DEFINE YOUR FUNCTIONS ABOVE
"""
def print_batch_amount():
    g_of_mochiko = int(input("Enter an amount (g) of mochiko: "))
    g_of_mochiko_each = 3 * 220
    g_of_sugar = int(input("Enter an amount (g) of sugar: "))
    g_of_sugar_each = 1.5 * 220
    g_of_cornstarch = int(input("Enter an amount (g) of cornstarch: "))
    g_of_cornstarch_each = 2 * 220
    g_of_anko = int(input("Enter an amount (g) of anko: "))
    g_of_anko_each = 220
    number_mochiko = g_of_mochiko // g_of_mochiko_each
    min_batch = number_mochiko
    number_sugar = g_of_sugar // g_of_sugar_each
    if number_sugar < min_batch:
        min_batch = number_sugar
    number_cornstarch = g_of_cornstarch // g_of_cornstarch_each
    if number_cornstarch < min_batch:
        min_batch = number_cornstarch
    number_anko = g_of_anko // g_of_anko_each
    if number_anko < min_batch:
        min_batch = number_anko

    print("With this amount of ingredients, you can make",min_batch, "batch(es) of 24 mochi.")


def main():
    """
    Just some sample behavior.
    """
    print_batch_amount()


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
