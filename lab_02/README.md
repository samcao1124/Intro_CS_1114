## CS-UY 1114 — Lab 2
# Karel and Control Flow
#### February 12th, 2021

You will need a working Karel environment installed on your computer for this lab. **If you need help with this, please
contact a teaching assistant or instructor ASAP!**

All lab work must be submitted within 24 hours of the start of your lab period on Gradescope (we will be checking this
using the timestamps of your last submission on GradeScope). This, of course, also means that if you submit a solution
before your allotted lab time, you will get no credit. You must try each problem at least once (that is, submitting at
least one attempt to GradeScope, whether it is correct or not). You are welcome to continue to work on the problems and
continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to remember to
submit your work.

Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on GradeScope, we will deduct 0.5 points
from the total 10-point value of the lab.

### Karel Restrictions

Your Karel programs are restricted to the language features as described in lectures 1-4. You may not use any other 
features of Python. Prohibited features include (but are not limited to) variables, parameters, operators, `for` loops, 
`break`, and `return`, even though the PyCharm-based version of Karel allows their use. 

### Karel Instruction Set

For your convenience, we are including Karel's native instruction set below:

|Function|Description|
|---|---|
|move()|Makes Karel move forward one square in the direction it is facing. Errors if there is a wall in front of Karel.|
|turn_left()|Makes Karel turn left.|
|pick_beeper()|Makes Karel pick up a beeper from the corner where it is currently standing. Errors if there are no beepers present on the corner.|
|put_beeper()|Makes Karel place a beeper on the corner where it is currently standing.|

And below, you will find the boolean expressions available for Karel programs:

|Function|Description|
|---|---|
|front_is_clear()|Is there no wall in front of Karel? Evaluates to `True` if answer is `Yes` and `False`, otherwise.|
|left_is_clear()|Is there no wall to Karel’s left? Evaluates to `True` if answer is `Yes` and `False`, otherwise.|
|right_is_clear()|Is there no wall to Karel’s right? Evaluates to `True` if answer is `Yes` and `False`, otherwise.|
|on_beeper()|Is there a beeper on the corner where Karel is standing? Evaluates to `True` if answer is `Yes` and `False`, otherwise.|
|facing_north()|Is Karel facing north? Evaluates to `True` if answer is `Yes` and `False`, otherwise.|
|facing_south()|Is Karel facing south? Evaluates to `True` if answer is `Yes` and `False`, otherwise.|
|facing_east|Is Karel facing east? Evaluates to `True` if answer is `Yes` and `False`, otherwise.|
|facing\_west()|Is Karel facing west? Evaluates to `True` if answer is `Yes` and `False`, otherwise.|
|||

### Problem 1: Infinite Loop
Let's, again, get started with something simple. Remember the track problem from lab 1?

![lab01_1](docs/images/lab02_1.png)

_**Figure 1**: Beginning state of world `lab_02_1.kwld`. This world can be accessed by choosing the configuration named
**`infinite_loop1`**._

Let's change it up a bit. As you can see, Karel will start facing east, in position (1, 1). Your first task is to write
instructions  that will allow Karel to run around a track, hugging the perimeter of the inner square, such as this
one, **forever** (i.e. Karel will never stop). Keep in mind that, while this track is 7x7, your instructions  should
work for tracks of any dimensions. That is, if Karel was placed in the following track, your program would still
work:

![lab01_1_2](docs/images/lab02_1_2.png)

_**Figure 2**: Beginning state of world `lab_02_1_2.kwld`. This world can be accessed by choosing the configuration named
**`infinite_loop2`**._

Your instructions should be implemented  in the function **`infinite_loop()`**, inside the file
[**infinite_loop.py**](infinite_loop.py).

### Problem 2: Picking Up Top Beepers
The next task will involve picking up beepers around the track. Karel will go around the track and pick up any beepers
along its way. Here's the catch: it should only pick up beepers if they are found on the top wall of the inner
square/rectangle, not including the corner positions:

![lab01_2](docs/images/lab02_2.png)

_**Figure 3**: Beepers that should and should not be picked up in world `lab_02_2.kwld`._

As in problem 1, your code *must* work for any sized world, with beepers placed anywhere along its perimeter.
Additionally, Karel will **not** go around the track forever, as in problem 1. Instead, once it reaches its original
position, it will stop moving! Keep in mind that Karel will start in position (1, 1), facing east, again. The starting
code can be found in file [**pick_up_top_beepers.py**](pick_up_top_beepers.py), in function **`pick_up_top_beepers()`**.
There are two worlds for you to test your code on, in this case. `lab_02_2.kwld` can be tested by selecting the
**`pick_up_top_beepers1`** configuration and world `lab_02_2_2.kwld` by selecting the **`pick_up_top_beepers2`**
configuration.

![lab01_2_2](docs/images/lab02_2_1.png)

_**Figure 3**: World `lab_02_2_1.kwld`._

It may also help to break your program down into individual functions if you are having trouble completing the task. 

### Problem 3: Paving Hurdles

Let's make things interesting now. Karel will be tasked with paving a road covered with hurdles of different sizes,
such as the one below:

![lab02_3_1](docs/images/lab02_3_1.png)

_**Figure 4**: Beginning state of world `lab_02_3_1.kwld`, accessible with the **`hurdles1`** configuration._

As you can see, Karel starts at position (1, 1), facing north. Additionally, Karel will always begin with a hurdle
immediately in front of it. Your task is to create a function **`pave_all_hurdles()`**, that will instruct Karel to walk
from its initial position, over each hurdle, dropping one beeper with every step until it reaches the right-most wall.
The ending state of the world after the `pave_all_hurdles()` function is executed  would look something like this:

![lab02_3_2](docs/images/lab02_3_2.png)

_**Figure 5**: World `lab_02_3_1.kwld` post-condition._

You may find it especially useful to break your program into several function to
accomplish this task, such as a function that will scale the hurdle vertically, a function that will travel between
hurdles, etc. It is ultimately up to you how you want to structure your code. You may find the starter code inside file
[**hurdles.py**](hurdles.py).

We've included a couple of different worlds for you to test your code with. Your code should world for each of these
worlds without any additional changes.

![lab02_3_3](docs/images/lab02_3_3.png)

_**Figure 6**: Beginning state of world `lab_02_3_2.kwld`, accessible with the **`hurdles2`** configuration._

![lab02_3_4](docs/images/lab02_3_4.png)

_**Figure 7**: Ending state of world `lab_02_3_2.kwld`._

![lab02_3_5](docs/images/lab02_3_5.png)

_**Figure 8**: Beginning state of world `lab_02_3_3.kwld`, accessible with the **`hurdles3`** configuration._

![lab02_3_6](docs/images/lab02_3_6.png)

_**Figure 9**: Ending state of world `lab_02_3_3.kwld`._

### Problem 4: Spiral (Optional)

_**Note**: For those who finished the problems above and want some extra practice, feel free to try problem 4 below. You
will not lose any points if you don't, so no stress!_

For this problem, Karel will begin in an east-facing position at (1, 1) in a world with a spiral such as this one:

![lab02_4_1](docs/images/lab02_4_1.png)

_**Figure 10**: Beginning state of world `lab_02_4_1.kwld`, accessible with the **`spiral1`** configuration._

We would like create a program that achieves the following ending state in this world:

![lab02_4_3](docs/images/lab02_4_3.png)

_**Figure 11**: Ending state of world `lab_02_4_1.kwld`._

Implement this program  inside the file [**spiral.py**](spiral.py), in function **`spiral()`** It may be helpful to break up your program
into three steps:

- Getting to the center:

![lab02_4_2](docs/images/lab02_4_2.png)

_**Figure 12**: Getting to the center of the spiral of world `lab_02_4_1.kwld`._

- Turning around

- Leaving the spiral, dropping beepers along the way.

This is, of course, not the only way to accomplish this task, but it may help to think of these tasks as "steps" towards the
full program. As with the last 3 problems, your code must work for any sized spiral, such as this one:

![lab02_4_4](docs/images/lab02_4_4.png)

_**Figure 13**: Beginning state of world `lab_02_4_2.kwld`, accessible with the **`spiral2`** configuration._

![lab02_4_5](docs/images/lab02_4_5.png)

_**Figure 14**: Ending state of world `lab_02_4_2.kwld`._

