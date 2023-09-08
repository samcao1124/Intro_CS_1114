## CS-UY 1114 — Lab 6
# String traversals, manipulation, and modules
#### Friday, March 12th, 2021

All lab work must be submitted within 24 hours of the start of your lab period on Gradescope (we will be checking this
using the timestamps of your last submission on Gradescope). This, of course, also means that if you submit a solution
before your allotted lab time, you will get no credit. You must try each problem at least once (that is, submitting at
least one attempt to Gradescope, whether it is correct or not). You are welcome to continue to work on the problems and
continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to remember to
submit your work.

Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on Gradescope, we will deduct 0.5 points
from the total 10-point value of the lab.

Remember that the points awarded by the autograder will not count towards your lab's final grade and will be removed
when the final grades are calculated.

---

### Problem 1: _I Fought The Law (of Cosines)_

Let's start with a (simple) calculator. Your goal is to create a function, **`get_gamma()`** in the file
[**law_of_cosines.py**](law_of_cosines.py), that will accept three arguments corresponding to the three sides of a triangle.
Then, according to the law of cosines, it will calculate and return angle _gamma_, in **degrees**:

![law_of_cosines](images/law_of_cosines.svg)

_**Figure 1**: Law of Cosines. [**(Source)**](https://en.wikipedia.org/wiki/Law_of_cosines)_

If the user enters any values that are less than or equal to zero, your function should return a **`-1`** as a result.
You may also want to consider whether the sides the user enters can actually
[**form a triangle**](https://en.wikipedia.org/wiki/Triangle_inequality). If they cannot, return **`-1`** in this case as well. Try breaking your program up into functions to accomplish this task! Keep in mind that the autograder
will only check the function **`get_gamma()`**. As long as your other functions are defined within the same file, they can be called from within 
**`get_gamma()`**!.

Naturally, you should take full advantage of the
[**math module**](https://docs.python.org/3/library/math.html) to accomplish this task—not only for trigonometric functions,
but also to convert results from one unit to another!

### Problem 2: _It's super effective!_

In the _Pokemon™_ game series, there is always a chance that your Pokemon will land a critical hit when attacking. This
basically means that, based on your Pokemon's stats, your attack **might** roughly double in damage. The "might" here is
actually based on probability:

> Whether a move scores a critical hit is determined by comparing a 1-byte **random number (0 to 255)** against a 1-byte
> threshold value (also 0 to 255); if the random number is less than the threshold, the Pokémon scores a critical hit.

— _[**Critical hit**](https://bulbapedia.bulbagarden.net/wiki/Critical_hit), Bulbapedia_.

Basically, we'll have two values:
- A random value, **`R`** from 0 to 255.
- A threshold value, **`T`** from 0 to 255. If this value is higher than **`R`**, the Pokemon lands a critical hit; we
can calculate this value as follows:

```text
T = (Pokemon_Speed / 2)
```
_**Figure 2**: Threshold formula, where **`Pokemon_Speed`** is equal to the Pokemon's speed stat._

If it is determined that the Pokemon has landed a critical hit, the damage multiplier (that is, the number by
which the Pokemon's attack will be multiplied by) will be equal to:

```text
M = (2L + 5) / (L + 5)
```
_**Figure 3**: Multiplier formula, where **`L`** is equal to the Pokemon's level._

With this knowledge in hand, write a function **`get_damage_multiplier()`** in the file
[**damage_multiplier.py**](damage_multiplier.py) that will accept the Pokemon's level and speed stat (both integer
values), and return the move's damage multiplier. You'll want to make use of the
[**random module**](https://docs.python.org/3/library/random.html) for this problem, and to think about what would happen if
the Pokemon _doesn't_ land a critical hit. You may assume that the Pokemon's level and speed stat will always be
positive integers.

You may assume in this problem that the Pokemon's level and speed stat will always be positive.

**NOTE**: When testing this function, you may want to keep in mind that procedures that involve randomness may need to be
tested several times in order to observe different behavior. Try changing your test values towards such  that they are more likely to land a critical hit.

### Problem 3: _Hidden Figures_

In the file [**hidden_figures.py**](hidden_figures.py), write a function called **`decode_by_skip()`** which will:

- Accept the following parameters:

| **Parameter** | **Type** | **Notes**                              |
|---------------|----------|----------------------------------------|
| `corpus`      | `str`   | A body of text.                        |
| `step`        | `int` | Optional. Default value should be `1`. |

_**Figure 2**: Parameters for `decode_by_skip`._

- Create a new string based on every `step`-th character in `corpus`.
- Return that new string.

For example, consider the following behavior:

```python
def main():
   test_corpus = "QnHTpSrGyXOodQpwvuYPzuvnicjNqdiKCzL KmnIFEKSijXuaoXNxp pykxh.VQwGokpwABnqhBSLitrXouuzlTIBm"
   test_step = 6
   test_decoded_string = get_decoded_string_by_skip(corpus=test_corpus, step=test_step)
   print(test_decoded_string)
```
Output:
```
Sound Euphonium
```

In other words, in this case, we consider every 6th character in the string `test_corpus`.

### Problem 4: _Goats Dream in Latin, Apparently_

_**NOTE**: You may **NOT** use the string method `split()` for this problem, as it creates a `list`, which we have not yet
covered in class. Trust me; you'll love `split()` all the more once you try this problem without it._

Write a function that accepts a single string, composed of words separated by spaces. Each word consists of lowercase
and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

- If a word begins with a vowel (`a`, `e`, `i`, `o`, or `u`), append `ma` to the end of the word.
For example, the word `apple` becomes `applema`.

- If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add `ma`.
For example, the word `goat` becomes `oatgma`.

- Add one letter `a` to the end of each word per its word index in the sentence, starting with the 1st word.
For example, the first word gets `a` added to the end, the second word gets `aa` added to the end and so on:

```python
def main():
   original_sentence = "I speak Goat Latin"
   goat_latin_translation = translate_sentence_to_goat_latin(original_sentence)
   print(goat_latin_translation)
```
Which results in:
```text
Imaa peaksmaaa oatGmaaaa atinLmaaaaa
```

Return the final sentence representing the conversion to Goat Latin. The function should be called
**`translate_sentence_to_goat_latin()`**, inside the file **[goat_latin.py](goat_latin.py)**. You may
assume the original sentence will contain **at least two words**.

**HINT**: The string method **`find()`** may be useful in this problem. You learned in lecture that `find()`
returns the first index where the `str` argument given to the `find()` method invocation is located in the `str` object on which the method is invoked. The method invocation returns -1 if the `str` is not contained in the `str` object on which the method is invoked:

```python
def main():
   some_string = "Bohemia has neither coasts nor a desert. Nice try, Shakespeare."
   period_index = some_string.find(".")
   exclamation_index = some_string.find("!")

   print(period_index)
   print(exclamation_index)

main()
```

This will display the following in your console:

```text
39
-1
```

That is, the index of the _first_ period (`.`) in the string `some_string` is 39, while the character `!` is not present in the `str` value referenced by `some_string`.

However, we can add extra arguments to the `find` function that will make our search more specific. The format is:
`find(character_we_are_searching, starting_point, ending_point)`.

For instance:

```python
def main():
   some_string = "Bohemia has neither coasts nor a desert. Nice try, Shakespeare. You almost had me."
   period_index = some_string.find(".")

   # If we wanted to find the location of any periods AFTER the first period...
   second_period_index = some_string.find(".", period_index + 1)  # we add a 1 because we want the second search to begin one index beyond where the previous period was found 

   # If we wanted to find the location of the first 's' in the second sentence...
   s_second_sentence_index = some_string.find("s", period_index + 1, second_period_index)

   print(second_period_index)
   print(s_second_sentence_index)

main()
```

Which will display the following on your console:
```text
62
56
```

We basically separated our original `some_string` by periods, `.`. So, keeping this in mind, which character would
You use to separate each word in your sentence?

You can find more detailed documentation for the
`find()` function [**here**](https://docs.python.org/2/library/string.html#string.find).

