"""
Topic: Sets in Python
---------------------
A set is an unordered, mutable collection of unique elements.
It automatically removes duplicates.
"""

# Example 1: Creating a set
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # 'apple' appears only once

# Example 2: Adding and removing elements
fruits.add("orange")
print(fruits)

fruits.remove("banana")  # removes 'banana'
print(fruits)

# Example 3: Using discard() — doesn’t throw error if not found
fruits.discard("grapes")

# Example 4: Looping through a set
for fruit in fruits:
    print(fruit)

# Example 5: Checking membership
print("apple" in fruits)
print("mango" not in fruits)

# Example 6: Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))         # all unique elements
print(a.intersection(b))  # common elements
print(a.difference(b))    # in a not in b
print(a.symmetric_difference(b))  # elements not common to both

# Example 7: Update methods
a.update(b)
print(a)  # adds all elements of b to a

# Example 8: Copying a set
c = fruits.copy()
print(c)

# Example 9: Clearing all elements
fruits.clear()
print(fruits)  # empty set

# Example 10: Creating empty set
empty_set = set()
print(type(empty_set))
