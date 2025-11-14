Dictionaries in Python
What is a Dictionary?

A dictionary is an unordered, mutable collection of key-value pairs.
It allows you to quickly access values using keys.

student = {
    "name": "Ketan",
    "age": 21,
    "course": "Python"
}

 Key Features of Dictionaries
Feature	Description
Unordered	Items have no fixed position (from Python 3.7+, insertion order is preserved)
Mutable	You can change, add, or remove items
Keys	Must be unique and immutable
Values	Can be of any data type
Access	Done using keys, not indexes

 Accessing and Modifying Values
print(student["name"])
print(student.get("course"))

student["age"] = 22
student["city"] = "Mumbai"

 Removing Elements
student.pop("city")
del student["age"]
student.clear()  # removes all items

Looping Through a Dictionary
for key in student:
    print(key, ":", student[key])


Or use:

for key, value in student.items():
    print(key, "=", value)

Useful Methods
Method	Description	Example
.keys()	Returns all keys	student.keys()
.values()	Returns all values	student.values()
.items()	Returns key-value pairs	student.items()
.get(key)	Returns value if key exists	student.get("name")
.pop(key)	Removes key-value pair	student.pop("age")

Nested Dictionaries
students = {
    "student1": {"name": "Ketan", "age": 21},
    "student2": {"name": "Bansuri", "age": 20}
}
print(students["student1"]["name"])  # Ketan

⚙️ Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)

 Advantages of Dictionaries

Fast lookups and updates (O(1) average)

Flexible — can store mixed data

Used in APIs, JSON data, configs, etc.

Foundation for Pandas DataFrames and JSON structures