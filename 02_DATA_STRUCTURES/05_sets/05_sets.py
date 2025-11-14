"""
Topic: Sets in Python
---------------------
A set is an unordered collection of unique elements.
It does not allow duplicates and supports mathematical set operations.
"""

# Example 1: Creating a set
numbers = {1, 2, 3, 4}
print(numbers)

# Example 2: No duplicates allowed
nums = {1, 2, 2, 3, 3, 4}
print(nums)   # duplicates removed

# Example 3: Adding elements
nums.add(5)
print(nums)

# Example 4: Removing elements
nums.remove(3)
nums.discard(10)   # won't give error
print(nums)

# Example 5: Set membership
print(2 in nums)
print(10 not in nums)

# Example 6: Set operations
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))         # union
print(A.intersection(B))  # intersection
print(A.difference(B))    # A - B
print(B.difference(A))    # B - A
print(A.symmetric_difference(B))

# Example 7: Iterating in a set
for item in A:
    print(item)

# Example 8: Converting list to set
lst = [1, 1, 2, 3, 4, 4]
unique = set(lst)
print(unique)

# Example 9: Frozen set (immutable set)
fs = frozenset([1, 2, 3])
print(fs)

# Example 10: Clearing a set
A.clear()
print(A)
