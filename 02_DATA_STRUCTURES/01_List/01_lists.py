"""
Topic: Lists in Python
----------------------
A list is an ordered, mutable (changeable) collection of items.
It can store elements of different data types.
"""

# Example 1: Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Example 2: Accessing list elements
print(fruits[0])   # first element
print(fruits[-1])  # last element

# Example 3: Modifying elements
fruits[1] = "mango"
print(fruits)

# Example 4: Adding elements
fruits.append("grapes")       # adds at end
fruits.insert(1, "kiwi")      # adds at position 1
print(fruits)

# Example 5: Removing elements
fruits.remove("apple")        # remove by value
removed_item = fruits.pop()   # remove last element
print("Removed:", removed_item)
print(fruits)

# Example 6: List slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # from index 1 to 3
print(numbers[:3])    # first 3 elements
print(numbers[-3:])   # last 3 elements

# Example 7: Looping through a list
for item in fruits:
    print(item)

# Example 8: Checking membership
print("mango" in fruits)
print("apple" not in fruits)

# Example 9: List methods
marks = [90, 75, 88, 92, 60]
print(len(marks))         # length
print(max(marks))         # maximum
print(min(marks))         # minimum
marks.sort()              # sort ascending
print(marks)
marks.reverse()           # reverse list
print(marks)

# Example 10: Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Access 6
