## CS-UY 1114 — Lab 5
# Function Parameters, `return`, and String Sequences
#### Friday, March 5th, 2021

All lab work must be submitted within 24 hours of the start of your lab period on Gradescope (we will be checking this
using the timestamps of your last submission on GradeScope). This, of course, also means that if you submit a solution
before your allotted lab time, you will get no credit. You must try each problem at least once (that is, submitting at
least one attempt to GradeScope, whether it is correct or not). You are welcome to continue to work on the problems and
continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to remember to
submit your work.

Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on GradeScope, we will deduct 0.5 points
from the total 10-point value of the lab.

### Introducing: The Lab Autograder!

From this lab forward, we will be leveraging GradeScope's autograder to help you check your work. Essentially, every
time you submit your work onto GradeScope, it will run all your functions through a few test cases that we have written
and let you know if it passed them or not. Remember, **labs are graded on completeness, not on correctness**, so don't
worry if your code doesn't pass all of the tests (you will still only be graded on whether you tried each problem or
not, in other words). This is just to help you check how well you are following the problem's directions. ***THE LABS
WILL STILL BE GRADED OUT OF 10, COMPLETELY BASED ON COMPLETENESS. THE POINTS THE AUTograder ON GRADESCOPE GIVES YOU
WILL NOT BE COUNTED TOWARDS YOUR GRADE!***

For the autograder to work, **both your files and functions must be spelled exactly  as  in this `README`,** so don't change any function or file names!

### Problem 1: _Signed, Sealed, Delivered, I'm Yours_

We'll start with a simple-ish problem to get us used to both the new function features you learned this week, and how
the autograder works.

In the file [**address_book.py**](address_book.py), write a function called **`get_formatted_address_string()`** that
will accept the following parameters:

| **Parameter Name** | **Type** | **Notes**                                                                           |
|--------------------|----------|-------------------------------------------------------------------------------------|
| `name`             | _`str`_  | Optional parameter, with the string `"Undisclosed Recipient"` as its default value. |
| `address`          | _`str`_  |                                                                                     |
| `city`             | _`str`_  |                                                                                     |
| `country`          | _`str`_  |                                                                                     |
| `postal_code`      | _`int`_  | Optional parameter, with the integer `0` as its default value.                      |

_**Table 1**: Parameters for the **`get_formatted_address_string()`** function._

Our function will then take these parameters, construct a nicely-formatted string (like you might see on an envelope),
***and return it***.

Here's how this program would work in practice:

```python
def main():
   test_name = "Herodotos of Halicarnassus"
   test_address = "Dionysiou Areopagitou 15"
   test_city = "Athens"
   test_country = "Greece"
   test_postal_code = 11742

   address_string = get_formatted_address_string(address=test_address, city=test_city, country=test_country,
                                                 name=test_name, postal_code=test_postal_code)

   print(address_string)
```
Output:
```text
Herodotos of Halicarnassus
Dionysiou Areopagitou 15
Athens, Greece
11742
```

A few things to note here:
- Two parameters, `name` and `postal_code`, have default values. If `name` defaults to its default value,
**include that default value in the final, formatted address**. If, for example, I hadn't passed a value for name in our
earlier function call, the final string would look like this:
```text
Undisclosed Recipient
Dionysiou Areopagitou 15
Athens, Greece
11742
```
- However, if the `postal_code` defaults to `0`, ***do not include it in the final, formatted string***. If I had not
passed a value for `postal_code` in the  earlier function call, then, the final, formatted string would look like this:
```text
Herodotos of Halicarnassus
Dionysiou Areopagitou 15
Athens, Greece
```
- Keep in mind that the autograder will not only test the above cases, but a variety of test values. You may assume that
the test values will be of the types specified in Table 1.

### Problem 2: Oh, how the (power) tables have turned

_**Note**: The autograder will not test this function, but you still need to attempt implementing this function to get full points!_

You have likely seen a multiplication-table such as the one below:

| **X**   | **1** | **2** | **3** | **4** | **5** |
|---------|-------|-------|-------|-------|-------|
| **1**   | 1     | 2     | 3     | 4     | 5     |
| **2**   | 2     | 4     | 6     | 8     | 10    |
| **3**   | 3     | 6     | 9     | 12    | 15    |
| **4**   | 4     | 8     | 12    | 16    | 20    |
| **5**   | 5     | 10    | 15    | 20    | 25    |

_**Figure 1**: A 5-by-5 Multiplication Table._

We will be generating something similar, but instead of using products, we will be using **powers**:

| **^** | **1** | **2** | **3** | **4** | **5** |
|-------|-------|-------|-------|-------|-------|
| **1** | 1     | 2     | 3     | 4     | 5     |
| **2** | 2     | 4     | 8     | 16    | 32    |
| **3** | 3     | 9     | 27    | 81    | 243   |
| **4** | 4     | 12    | 64    | 16    | 256   |
| **5** | 5     | 25    | 125   | 625   | 3125  |

_**Figure 2**: A 5-by-5 Power Table._

We want to **nicely** print a 5-by-X power table in our console. In the file
[**by_five_power_table.py**](by_five_power_table.py), write a function called **`print_by_five_power_table()`** that
will accept a single integer variable (named `height`) and print a `height`-by-5 table onto your console:

```python
def main():
   test_height = 3
   print_by_five_power_table(test_height)

main()
```
Output:
```text
1  1  1  1  1
2  4  8  16 32
3  9  27 81 243
```
Nicely spaced out, right? Now consider using `4` as a `test_height`?
```text
1  1  1  1  1
2  4  8  16 32
3  9  27 81 243
4  16 64 256    1024
```
(**Hint**: utilize `print`'s `sep` parameter.)

If the user chooses not to enter a value for the height, **`print_by_five_power_table()`** should default to `5`.

By the way, after a certain number, the spacing starts looking a bit funky. This is fine for our purposes. The
important part is that you manage to make this program modular height-wise. The keen eyes amongst you may have noticed
that this problem involves a bit of hard-coding (i.e. magic numbers) in terms of the width of the table. This, too, is
fine for now. We will learn how to make the width modular as well in the coming lectures.



### Problem 3: Password Checker

Write a function, **`is_password_valid()`**, that checks whether the string parameter argument `password` is valid.
The rules for password validity are as follows:
1. Must include at least 8 characters.
2. Must include at least 2 lowercase letters.
3. Must include at least 2 uppercase letters.
4. Must include at least 1 number.
5. Must include at least 1  of the following non-alphanumeric characters: `!`, `@`, `#`, or `$`.

If the user's password is valid, your function will return **`True`**. Otherwise, it will return **`False`**. You can
find the starter code in the file **[password_checker.py](password_checker.py)**.

```python
def main():
   test_password = "NAit1!"

   if password_checker(test_password):
       # password_checker() returned True
       print("This is a valid password!")
   else:
       # password_checker() returned False
       print("This is not a valid password!")

main()
```
Which displays the following in your console:
```text
This is not a valid password!
```

**Hint**: An uppercase letter is a character that is greater than or equal to `A` and less than or equal to `Z`. A
lowercase letter is a character that is greater than or equal to `a` and less than or equal to `z`, etc.

You may assume the parameter `password` does not have a default value.

### Problem 4: DNA Sequencing

The starter code can be found in the file **[get_fused_sequence_complement.py](get_fused_sequence_complement.py)**.

Given two DNA sequences represented as string values, write a function, **`get_fused_sequence_complement()`**, that will:

1. Fuse the two sequences by adding a nucleotide from each in alternating order (i.e. `ACT` + `CA` = `ACCAT`). If any
invalid nucleotides (i.e., not A, C, T, or G) are found in either sequence, you should ignore them and not include them
in the fused sequence.
2. Create a complement sequence from the new, fused sequence. (i.e `ACCAT` complements to `TGGTA`)
3. Return that complement sequence.

Recall the DNA complements:

| **Nucleotide** | **Complement** |
|----------------|----------------|
| A              | T              |
| C              | G              |
| T              | A              |
| G              | C              |

_**Figure 1**: [**Nucleotide
Complements**](
https://en.wikipedia.org/wiki/Complementarity_(molecular_biology)#DNA_and_RNA_base_pair_complementarity)._

Here's another example to make it clearer:

```python
def main():
   sequence_a = "ACTGGGTA"
   sequence_b = "TTZAG"
   fused_sequence_complement = get_fused_sequence_complement(sequence_a, sequence_b)
   print(fused_sequence_complement)

main()
```

Which will output the following to your console:

```text
TAGAACTCCCAT
```

You may assume that both DNA sequences will always be valid, uppercase Python strings, and not an `int`, `float`, etc.
You may also find it useful to break this problem up into smaller functions. For instance, a function that takes a single
nucleotide and returns its complement could be useful:

```python
def get_complement(nucleotide):
   """
   Returns a character representing the complement of a nucleotide.

   :param nucleotide: A character representing a nucleotide
   :return: A character representing a nucleotide's complement
   """
   # some code...
   # some code...
   # some code...

nucleotide = 'A'
complement = get_complement(nucleotide)

print(complement)
```
Output:
```text
T
```
(This is, of course, not necessary. The autograder will only be checking **`get_fused_sequence_complement()`**!)

Once you have implemented this function, you can traverse your original nucleotide sequence and construct a new string based on the results that `get_complement()` returns.


