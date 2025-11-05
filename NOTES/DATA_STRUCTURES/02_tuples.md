# Tuples in Python

## What is a Tuple?
A **tuple** is an ordered collection of items, similar to a list,  
but **immutable** (cannot be changed once created).

```python
fruits = ("apple", "banana", "cherry")
Key Features of Tuples
Feature	Description
Ordered	Elements have a fixed order
Immutable	Cannot change, add, or remove elements
Allows Duplicates	Yes
Can Contain Multiple Data Types	Yes
Accessing Elements

Use index positions just like lists.

print(fruits[0])   # apple
print(fruits[-1])  # cherry

Tuple with Different Data Types
mixed = (1, "hello", 3.5, True)

Nested Tuples

Tuples can contain other tuples.

nested = (1, 2, (3, 4, 5))
print(nested[2][1])  # 4

Tuple Unpacking

Assign tuple values to variables in a single line.

numbers = (10, 20, 30)
a, b, c = numbers
print(a, b, c)

Looping Through Tuples
for fruit in fruits:
    print(fruit)

Tuple Methods
Method	Description	Example
.count(x)	Returns the number of times x appears	marks.count(90)
.index(x)	Returns index of first occurrence	marks.index(100)
Converting Tuple to List

Tuples are immutable, but we can convert them to a list, modify, and convert back.

t = (1, 2, 3)
temp = list(t)
temp.append(4)
t = tuple(temp)
print(t)

Single Element Tuple

To define a single element tuple, use a comma:

single = ("apple",)
print(type(single))  # <class 'tuple'>


Without the comma, it’s not a tuple:

not_tuple = ("apple")
print(type(not_tuple))  # <class 'str'>

Advantages of Tuples

Faster than lists (performance)

Safer (data cannot be changed accidentally)

Can be used as keys in dictionaries