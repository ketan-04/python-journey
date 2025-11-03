"""
Topic: Loops in Python
----------------------
Loops are used to repeat a block of code multiple times.
Python mainly has two types of loops:
1. for loop
2. while loop
"""

# Example 1: for loop with range()
for i in range(5):
    print("Hello Python", i)

# Example 2: for loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 3: using break
for num in range(1, 6):
    if num == 3:
        break  # stops the loop when num is 3
    print(num)

# Example 4: using continue
for num in range(1, 6):
    if num == 3:
        continue  # skips number 3
    print(num)

# Example 5: nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Example 6: while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Example 7: while loop with break
x = 1
while True:
    print(x)
    if x == 5:
        break
    x += 1

# Example 8: while loop with continue
y = 0
while y < 5:
    y += 1
    if y == 3:
        continue
    print("y =", y)
