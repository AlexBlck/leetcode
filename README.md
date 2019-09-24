# Leetcode Practice
This is my diary for leetcode practice, roughly following the instructions
provided by [Siraj](https://youtu.be/sMkMr2455mk). I am an MSc Machine Learning
student and my first degree is in Physics, so this is my way of filling in the
gaps in my CS knowledge.

## [Intro to Data Structures and Algorithms](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513)

### Lesson 1 - Introduction and Efficiency
Not much new here, basic Python refresher and intro to O(n) notation. I've had
my fair share of that in [Cracking the Coding Interview](https://www.amazon.co.uk/Cracking-Coding-Interview-6th-Programming/dp/0984782850).

### Lesson 2 - List-Based Collections
Excercises asked to make classes that represent data structures: linked lists,
stacks and queues. Got everything right, but for a more elegant solution I need
to remember that Python lists have `pop()` built in.

### Lesson 3 - Searching and Sorting
Binary search, recursion, bubble sort (naive approach), merge sort (divide and
conquer), quick sort (pivot). Implementing quick sort took some time, but was
definitely rewarding. I need to remember array slicing inclusive/non-inclusive
rules better, so that I don't need to open an extra document and try it out every
time.

### Leetcode 905: Sort Array by Parity
First solution turned out to be the fastest. Then tried to be clever and do an
in-place version as well. A bit slower, but better space complexity. Using `sort()`
with a lambda function solves this problem in one line.
