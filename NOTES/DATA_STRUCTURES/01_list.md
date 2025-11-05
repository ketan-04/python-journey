# Lists in Python

## What is a List?
A **list** is an ordered, mutable collection of items.  
It can contain different data types (numbers, strings, etc.).

```python
fruits = ["apple", "banana", "cherry"]
Accessing Elements

Use index positions (starting from 0).

print(fruits[0])   # apple
print(fruits[-1])  # cherry

Modifying Lists

Lists are mutable, so we can change their elements.

fruits[1] = "mango"
print(fruits)

# Adding Elements
# Method	Description	Example
.append(x)	Add at end	fruits.append("grapes")
.insert(i, x)	Add at index	fruits.insert(1, "kiwi")
.extend(list)	Add another list	fruits.extend(["papaya", "melon"])
Removing Elements
Method	Description	Example
.remove(x)	Removes the first occurrence of x	fruits.remove("apple")
.pop()	Removes last element	fruits.pop()
del list[i]	Deletes element at index	del fruits[0]
Slicing Lists

Extract a portion of a list.

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[-3:])   # [30, 40, 50]

Looping Through Lists
for fruit in fruits:
    print(fruit)

Common List Functions
Function	Description	Example
len(list)	Number of items	len(fruits)
max(list)	Largest value	max(marks)
min(list)	Smallest value	min(marks)
list.sort()	Sort list	marks.sort()
list.reverse()	Reverse order	marks.reverse()
Nested Lists

A list inside another list.

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])  # 6