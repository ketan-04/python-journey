Sets in Python
What is a Set?

A set is an unordered collection of unique elements.
It automatically removes duplicates and supports mathematical set operations.

numbers = {1, 2, 3, 4}

✨ Key Features
Feature	Description
Unordered	No index positions
Unique elements	Duplicate not allowed
Mutable	Can add or remove elements
Fast lookup	Uses hash-based structure
🔹 Creating a Set
nums = {1, 2, 2, 3, 4}
print(nums)   # duplicates removed

🔧 Adding & Removing
nums.add(5)
nums.remove(3)
nums.discard(10)   # no error

🔍 Membership Test
print(2 in nums)
print(10 not in nums)

➗ Set Operations
Operation	Code	Meaning
Union	A.union(B)	All elements from both
Intersection	A.intersection(B)	Common elements
Difference	A.difference(B)	Elements in A not in B
Symmetric Difference	A.symmetric_difference(B)	Except common
🔁 Looping
for item in A:
    print(item)

🔄 Converting List to Set
unique = set([1,1,2,3])

🧊 Frozen Set

Immutable version of set:

fs = frozenset([1, 2, 3])

📝 Practice Questions

Remove duplicates from a list using a set.

Find union and intersection of two sets.

Write a program to check if two sets are disjoint.

Convert a set to a list and sort it.

Use a frozenset inside a dictionary.

🧾 Summary

Set = unique + unordered

Supports fast operations

Great for mathematical set calculations

Frozen set = immutable set