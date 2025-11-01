# 🧠 Type Casting in Python

### 🔹 What is Type Casting?
Type casting (or **type conversion**) means converting one data type into another.  
It’s used when you need to perform operations between incompatible data types.

---

### 🔹 1. Implicit Type Casting
Python **automatically** converts data types during operations.

```python
a = 5      # int
b = 2.5    # float
c = a + b  # int + float → float
print(c)   # 7.5
print(type(c))  # <class 'float'>
