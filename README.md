# Leetcode Practice
This is my diary for leetcode practice, roughly following the instructions
provided by [Siraj](https://youtu.be/sMkMr2455mk). I am an MSc Machine Learning
student and my first degree is in Physics, so this is my way of filling in the
gaps in my CS knowledge.

## [Intro to Data Structures and Algorithms](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513)

##### 23.09.2019:
### Lesson 1 - Introduction and Efficiency
Not much new here, basic Python refresher and intro to O(n) notation. I've had
my fair share of that in [Cracking the Coding Interview](https://www.amazon.co.uk/Cracking-Coding-Interview-6th-Programming/dp/0984782850).

### Lesson 2 - List-Based Collections
Excercises asked to make classes that represent data structures: linked lists,
stacks and queues. Got everything right, but for a more elegant solution I need
to remember that Python lists have `pop()` built in.

##### 24.09.2019:
### Lesson 3 - Searching and Sorting
Binary search, recursion, bubble sort (naive approach), merge sort (divide and
conquer), quick sort (pivot). Implementing quick sort took some time, but was
definitely rewarding. I need to remember array slicing inclusive/non-inclusive
rules better, so that I don't need to open an extra document and try it out every
time.

##### 27.09.2019:
### Lesson 4 - Maps and Hashing
This is where things start to get interesting and I am more outside of my
comfort zone.

#### Quiz: Python Dictionaries
The task was to produce certain outputs, given a dictionary with cities, countries
and continents. I have overcomplicated my solution for output of 'All cities in
Asia, in alphabetic order, next to the name of the country'. Here is what I did:
```python
city_list = []
for country, city in zip(locations['Asia'].keys(), locations['Asia'].values()):
    city_list.append((country, city))

city_list.sort(key = lambda x: x[1])
for country, city in city_list:
    print(city[0] + " - " + country)
```
It does solve the problem, but there are two things to keep in mind for the future:
* Use `dict.iteritems()` instead of `zip(dict.keys(), dict.values())`
* Read the task more carefully. The output had to be a city followed by a country,
not the other way around. So there was no need in a `sort(key = lambda x: x[1])`.
All I had to do is create a list of strings and sort them alphabetically. But it
was still nice to make use of what I learned in Leetcode 905.

##### 29.09.2019:
#### Quiz: String Keys Practice
This excercise alone is definitely not enough to solidify the whole concept of
hashing. I will definitely do a bunch of problems on hashmaps in the nearest future.

### Lesson 5 - Trees
It looks like trees in this course are described in much more depth (no pun
intended) than the previous topics.
## Leetcode Problems
In the description of every problem I am trying to outline one thing, knowledge
of which would have made the solution easier. Problems within each difficulty
level are listed in chronological order.
### Easy
#### 905: [Sort Array by Parity (24.09.2019)](https://leetcode.com/problems/sort-array-by-parity/)
First solution turned out to be the fastest. Then tried to be clever and do an
in-place version as well. A bit slower, but better space complexity. Using `sort()`
with a lambda function solves this problem in one line.
#### 811: [Subdomain Visit Count (27.09.2019)](https://leetcode.com/problems/subdomain-visit-count/)
By serendipity, I started this problem right after I went through dictionaries
in a Udacity course. Proposed solution uses `collections.Counter()`. I was not
aware of the existance of it, so my solution basically reinvents `Counter`'s
functionality. Otherwise, it's pretty similar.
#### 888: [Fair Candy Swap (30.09.2019)](https://leetcode.com/problems/fair-candy-swap/)
My first brute force solution had a runtime of [2872ms](https://leetcode.com/submissions/detail/265615443/), while the median was around
425ms. My second attempt got me to [1352ms](https://leetcode.com/submissions/detail/265616527/). At this point I decided to bring out
the big guns and took a pen and some paper. Also, I looked up the best way to get
rid of duplicates in a list on [StackOverflow](https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists). This time I achieved [780ms](https://leetcode.com/submissions/detail/265617544/). Today I
learned that even if the code looks obvious, it might be a good idea to read
a description the author of an answer has given. I simply copied tho whole
`list(set(A))`. Just by removing the `list` cast I cut my runtime to an acceptable
[420ms](https://leetcode.com/submissions/detail/265618845/).
