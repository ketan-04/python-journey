"""
Topic: Type Casting in Python
---------------------------------
Type casting means converting one data type into another.
Python allows both implicit and explicit type conversions.
"""

# 🔹 Example 1: Implicit Type Casting
# (Python automatically converts data types)
a = 5
b = 2.5
c = a + b   # int + float → float
print("Implicit Casting Result:", c)
print("Type of c:", type(c))

# 🔹 Example 2: Explicit Type Casting
# (You manually convert data types)
x = int(10.8)     # float to int
y = float(5)      # int to float
z = str(100)      # int to string

print("\nExplicit Type Casting:")
print("x =", x, "| Type:", type(x))
print("y =", y, "| Type:", type(y))
print("z =", z, "| Type:", type(z))

# 🔹 Example 3: String to Integer (only if string is numeric)
num_str = "50"
num_int = int(num_str)
print("\nString to Int:", num_int + 10)

# 🔹 Example 4: Invalid Conversion (will cause error)
try:
    invalid = int("Hello")   # not a numeric string
except ValueError as e:
    print("\nError Example:", e)
