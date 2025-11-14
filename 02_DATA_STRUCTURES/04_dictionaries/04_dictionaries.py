"""
Topic: Dictionaries in Python
-----------------------------
A dictionary is an unordered, mutable collection of key-value pairs.
Each key must be unique and immutable (like string, number, or tuple).
"""

# Example 1: Creating a dictionary
student = {
    "name": "Ketan",
    "age": 21,
    "course": "Python"
}
print(student)

# Example 2: Accessing values
print(student["name"])
print(student.get("course"))

# Example 3: Adding and updating items
student["age"] = 22
student["city"] = "Mumbai"
print(student)

# Example 4: Removing items
student.pop("city")
print(student)

# Example 5: Looping through a dictionary
for key in student:
    print(key, ":", student[key])

# Example 6: Keys, Values, and Items
print(student.keys())
print(student.values())
print(student.items())

# Example 7: Nested dictionaries
students = {
    "student1": {"name": "Ketan", "age": 21},
    "student2": {"name": "Bansuri", "age": 20}
}
print(students["student1"]["name"])

# Example 8: Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)

# Example 9: Using dict() constructor
info = dict(name="Ravi", age=25, country="India")
print(info)

# Example 10: Checking membership
print("name" in student)
print("marks" not in student)
