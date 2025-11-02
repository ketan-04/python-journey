"""
Topic: Conditional Statements in Python
---------------------------------
Conditional statements let your program make decisions
based on certain conditions (True/False).
"""

# 🔹 Example 1: Basic if statement
age = 18
if age >= 18:
    print("You are eligible to vote!")

# 🔹 Example 2: if-else statement
marks = 45
if marks >= 50:
    print("You passed the exam ")
else:
    print("You failed the exam ")

# 🔹 Example 3: if-elif-else ladder
temperature = 32

if temperature > 35:
    print("It's too hot ")
elif temperature < 15:
    print("It's too cold ")
else:
    print("Weather is pleasant ")

# 🔹 Example 4: Nested if
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful ")
    else:
        print("Incorrect Password ")
else:
    print("User not found!")

# 🔹 Example 5: Real-life mini example
balance = 1200
withdraw = 1500

if withdraw <= balance:
    print("Transaction successful ")
else:
    print("Insufficient balance ")
