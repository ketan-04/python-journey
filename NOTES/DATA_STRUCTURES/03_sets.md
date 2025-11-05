# Sets in Python

## What is a Set?
A **set** is an unordered collection of unique elements.  
It is **mutable** (you can add or remove items) but **doesn’t allow duplicates**.

```python
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # {'apple', 'banana', 'cherry'}
Key Features of Sets
Feature	Description
Unordered	No fixed index position
Mutable	Can add or remove items
No Duplicates	Automatically removes duplicates
Heterogeneous	Can contain multiple data types

Creating a Set
python
Copy code
my_set = {1, 2, 3}
empty = set()  # Correct way for an empty set
❌ {} creates an empty dictionary, not a set.

Adding and Removing Elements
python
Copy code
fruits.add("orange")
fruits.remove("banana")
fruits.discard("grapes")  # doesn’t throw error if not found
Accessing Elements
Sets don’t support indexing or slicing because they are unordered.
Use loops or membership tests instead.

python
Copy code
for item in fruits:
    print(item)

print("apple" in fruits)
Set Operations
Python sets are great for mathematical operations:

Operation	Method	Example	Output
Union	a.union(b)	{1,2,3}.union({3,4})	{1,2,3,4}
Intersection	a.intersection(b)	{1,2,3}.intersection({2,3})	{2,3}
Difference	a.difference(b)	{1,2,3}.difference({2,3})	{1}
Symmetric Difference	a.symmetric_difference(b)	{1,2,3}.symmetric_difference({2,3,4})	{1,4}

Updating a Set
python
Copy code
a = {1, 2, 3}
b = {3, 4, 5}
a.update(b)
print(a)  # {1, 2, 3, 4, 5}
Copying and Clearing
python
Copy code
new_set = a.copy()
a.clear()
print(a)  # set()
Common Use Cases
Removing duplicates from a list

Performing mathematical set operations

Fast membership checking (in / not in)

Practice Questions
Create a set of 5 colors and remove one using discard().

Perform union and intersection on two sets {1,2,3} and {3,4,5}.

Convert a list with duplicate numbers into a set.

Write a program to find elements common in two sets.

Create an empty set and verify its type.

Summary
Sets are unordered and mutable but don’t allow duplicates.

Common methods: add(), remove(), discard(), union(), intersection().

Best for mathematical and membership operations.