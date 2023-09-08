## CS-UY 1114 — Lab 4
# User Input and `for` Loops
#### February 26th, 2021


All lab work must be submitted within 24 hours of the start of your lab period on Gradescope (we will be checking this
using the timestamps of your last submission on GradeScope). This, of course, also means that if you submit a solution
before your allotted lab time, you will get no credit. You must try each problem at least once (that is, submitting at
least one attempt to GradeScope, whether it is correct or not). You are welcome to continue to work on the problems and
continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to remember to
submit your work.

Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on GradeScope, we will deduct 0.5 points
from the total 10-point value of the lab.

### Restrictions

The Python structures that you use in this lab should be restricted to those you have learned in lecture so far. Please
check with your teaching assistants in case you are unsure whether something is or is not allowed!

### Problem 1: I've Got The Power(s)

Let's start with something simple (though maybe not as simple as it may seem at first glance), as is our custom. In the
file [**powers_of.py**](powers_of.py), write a function called **`print_powers_of()`** that will:

1. ask the user for two **positive integers**, a `base`, and a `power`, and
2. print, one by one, the result of raising that base by every power from 0 to `power`.

Here's an example of a function call to the `print_powers_of()` function:

```python
def main():
    print_powers_of()

main()
```
If, for example, the use enters `2` and `7`:
```text
Please enter a positive integer to serve as the base: 2
Please enter a positive integer to serve as the highest power: 7
2 ^ 0 = 1
2 ^ 1 = 2
2 ^ 2 = 4
2 ^ 3 = 8
2 ^ 4 = 16
2 ^ 5 = 32
2 ^ 6 = 64
2 ^ 7 = 128
```
If the user instead enters `10` and `3`:
```
Please enter a positive integer to serve as the base: 10
Please enter a positive integer to serve as the highest power: 3
10 ^ 0 = 1
10 ^ 1 = 10
10 ^ 2 = 100
10 ^ 3 = 1000
```
A few things to keep in mind:
- You may assume the user input will be numerical.
- Since the options for the `base` and the highest `power` are literally infinite, the use of a **loop** will come in 
very handy. 
- If the user attempts to enter a negative number into your program, **print an error message instead of the
list of powers.**
- If the user attempts to enter a non-integer into your program, **print an error message instead of the
list of powers.** There's a few ways to check for this, but make sure it's something that you have learned in class
already! (`%`, `//` and `==`; i.e. do *not* use `round()` or the `math` module. That's no fun.)

```text
Please enter a positive integer to serve as the base: 3.4
Please enter a positive integer to serve as the highest power: 4
ERROR: Both values must be POSITIVE INTEGERS.
```
```
Please enter a positive integer to serve as the base: -345324325436
Please enter a positive integer to serve as the highest power: 2
ERROR: Both values must be POSITIVE INTEGERS.
```

### Problem 1.5: (s)rewoP ehT toG ev'I (Optional)

While this problem is optional, I ***strongly*** recommend you give it a shot after you finish the lab for extra 
practice with `for` loops!

The task is to write a function named **`print_even_powers_of_in_reverse()`**, also in the file 
[**powers_of.py**](powers_of.py) that will, as the name implies, do exactly the same thing as `print_powers_of()`, but
it will only print the ***even*** (i.e. 2, 4, 6, etc.) powers of the `base`, and will do so backwards.

For example, the execution of the following code:

```python
def main():
    print_even_powers_of_in_reverse()

main()
```
will result in the following behavior:
```text
Please enter a positive integer to serve as the base: 7
Please enter a positive integer to serve as the highest power: 13
7 ^ 12 = 13841287201
7 ^ 10 = 282475249
7 ^ 8 = 5764801
7 ^ 6 = 117649
7 ^ 4 = 2401
7 ^ 2 = 49
7 ^ 0 = 1
```

The same rules and restrictions for problem 2 apply here. The solutions to problem 1 and 1.5 are not very different,,
so you will not need to change too much from the original code!

### Problem 2: How old are Saturnians?

It takes Saturn approximately 10,759 Earth-days to orbit the sun. In the file 
**[saturnian_to_earth_age_converter.py](saturnian_to_earth_age_converter.py)**, write a function 
**`print_earth_age()`** that will translate a Saturnian's age into Earth units. Take a look at the sample behavior below:

```text
How old is the Saturnian you are talking to? 10
This Saturnian is 294 Earth-years, 9 Earth-months, and 10 Earth-days old.
```

For this problem, you may assume that Earth-years are always 365 days long, and Earth-months are always 30 days long.

### Problem 3: Thrifty Programmer

In the file [**price_calculator.py**](price_calculator.py), write a function named **`get_final_price()`** that will:

1. Accept price amounts from the user *until* the total amount reaches $1,000.
2. New York State sales tax will then be added to the final total price (0.08%).
3. If the total amount of items is greater than 10, then the total price will receive a 20% discount, **post-tax**.

Note that the actual total can go over $1000.00 if the price of the last item makes the total go over 1000. Your program
must simply stop once the total is greater than or equal to 1000.

For example, consider the following program:

```python
def main():
    get_final_price()

main()
```
Output in case that more than 10 items were bought:
```text
Enter the price of your item: 10
Enter the price of your item: 20
Enter the price of your item: 30
Enter the price of your item: 40
Enter the price of your item: 50
Enter the price of your item: 60
Enter the price of your item: 70
Enter the price of your item: 80
Enter the price of your item: 90
Enter the price of your item: 100
Enter the price of your item: 110
Enter the price of your item: 120
Enter the price of your item: 130
Enter the price of your item: 140
20% Discount applied!
The total price is $907.2
```
Notice that I added an extra `print()` function call to produce the discount message (`20% Discount applied!`) just to make things clearer. Feel free to do
this as well.

If no discount was applied:
```text
Enter the price of your item: 100
Enter the price of your item: 200
Enter the price of your item: 300
Enter the price of your item: 400
The total price is $1080.0
```

### Problem 4: Tamako Market

In this program, we're going to use Python to calculate how many [***mochi***](https://en.wikipedia.org/wiki/Mochi) we 
can make using a certain amount of ingredients. A basic recipe for a batch of 24 pieces of
[***daifuku mochi***](https://en.wikipedia.org/wiki/Daifuku) calls for:
- 3 cups of sweet rice flour (_mochiko_)
- 1.5 cups of sugar
- 2 cups of cornstarch
- 1 cup of red bean paste ([***anko***](https://en.wikipedia.org/wiki/Red_bean_paste))

Your program will work is as follows:

1. The user will enter a certain amount of _mochiko_, sugar, cornstarch, and _anko_ in ***grams***.
2. The program will then convert those gram amounts to cups (1 cup = 220g).
3. The program will then calculate how many batches of _daifuku mochi_ can be made with this quantity of ingredients.

Implement this program in the file [**ingredient_calculator.py**](ingredient_calculator.py), within a function named 
**`print_batch_amount()`**. A sample program execution could look like this:

```python
def main():
    print_batch_amount()

main()
```
Output:
```text
Enter an amount (g) of mochiko: 2500
Enter an amount (g) of sugar: 3400
Enter an amount (g) of cornstarch: 5000
Enter an amount (g) of anko: 3200
With this amount of ingredients, you can make 3 batch(es) of 24 mochi.
```

You may assume the user will always enter positive numerical amounts.

This problem may be deceptively hard to wrap your head around, so refer the the following hints if you're having
trouble (and/or ask your lovely TAs for help):

1. Start with a 0 amount of batches.
2. Determine whether the amount of cups of every ingredient is enough for a **single** batch of _mochi_ for **every 
ingredient** (for example, if you have 10 cups of _mochiko_, you know you have enough for a **single** batch, at least).
3. If you have enough cups of **every ingredient** for a **single** batch of mochi, increase the number of batches by
1, and subtract the amount you just used of **every ingredient** from the total amount (for example, if you had 10 cups
of mochiko, after making one batch, you are left with 7 cups of mochiko available).
4. Reassess if the leftover amount of **every ingredient** is enough for another batch (Hint: this is either `True`
or `False`).
5. Repeat steps 3-4 ***while*** step 4 is `True`.

Feel free to edit this program after lab to match your own recipes! This is what makes programming fun!

![mochi](docs/images/mochi.gif)

