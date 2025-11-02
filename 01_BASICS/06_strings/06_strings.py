"""
Topic: Strings in Python
------------------------
A string is a sequence of characters enclosed in single or double quotes.
"""

# Example 1: Creating strings
name = "Leeladhar"
greeting = 'Hello'
print(name)
print(greeting)

# Example 2: Multi-line string
intro = """My name is Leeladhar.
I am learning Python.
"""
print(intro)

# Example 3: String concatenation
first_name = "Leeladhar"
last_name = "Sharma"
full_name = first_name + " " + last_name
print(full_name)

# Example 4: String indexing and slicing
text = "Python"
print(text[0])     # First character
print(text[-1])    # Last character
print(text[0:3])   # Characters from index 0 to 2
print(text[:4])    # First 4 characters

# Example 5: String methods
message = " hello python "
print(message.upper())      # Convert to uppercase
print(message.lower())      # Convert to lowercase
print(message.strip())      # Remove extra spaces
print(message.replace("python", "world"))  # Replace text
print(message.find("python"))              # Find index

# Example 6: f-strings (formatted string literals)
age = 21
print(f"My name is {name} and I am {age} years old.")

# Example 7: Checking substrings
sentence = "Learning Python is fun"
print("Python" in sentence)     # True
print("Java" not in sentence)   # True


intro = """This is
a multi-line string."""


# String Concatenation

# Joining two or more strings using +.

first = "Hello"
last = "World"
print(first + " " + last)


# Indexing and Slicing

# Strings are indexed starting from 0.

text = "Python"
print(text[0])   # P
print(text[-1])  # n
print(text[0:3]) # Pyt


# f-Strings (Formatted Strings)

# Used for inserting variables inside strings.

name = "Leeladhar"
age = 21
print(f"My name is {name} and I am {age} years old.")

# Checking Substrings
sentence = "Learning Python is fun"
print("Python" in sentence)   # True
print("Java" not in sentence) # True