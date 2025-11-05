"""
Topic: Tuples in Python
-----------------------
A tuple is an ordered, immutable (unchangeable) collection of items.
It is similar to a list but once created, its elements cannot be changed.
"""

# Example 1: Creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Example 2: Accessing elements
print(fruits[0])     # first element
print(fruits[-1])    # last element

# Example 3: Tuple with different data types
mixed = (1, "hello", 3.5, True)
print(mixed)

# Example 4: Nested tuple
nested = (1, 2, (3, 4, 5))
print(nested[2][1])  # Access 4

# Example 5: Tuple unpacking
numbers = (10, 20, 30)
a, b, c = numbers
print(a, b, c)

# Example 6: Iterating through a tuple
for item in fruits:
    print(item)

# Example 7: Checking membership
print("apple" in fruits)
print("grapes" not in fruits)

# Example 8: Tuple methods
marks = (85, 90, 75, 90, 100)
print(marks.count(90))   # count occurrences
print(marks.index(100))  # find index

# Example 9: Converting tuple to list
t = (1, 2, 3)
temp = list(t)
temp.append(4)
t = tuple(temp)
print(t)

# Example 10: Single element tuple
single = ("apple",)   # must have a comma
print(type(single))
