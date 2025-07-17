"""
A tuple is an ordered, immutable collection of values.
They are typically used for:

Fixed data groupings

Returning multiple values from functions

Lightweight, read-only data structures

| Feature    | Value              |
| ---------- | ------------------ |
| Ordered    | ✅ Yes              |
| Indexable  | ✅ Yes (like lists) |
| Mutable    | ❌ No (Immutable)   |
| Duplicates | ✅ Allowed          |
| Nesting    | ✅ Supported        |


# Single item or an elemnet in a tuple need a comma
x = (5)       # ❌ This is just an int!
y = (5,)      # ✅ This is a tuple with one element

| Feature            | List                | Tuple                                         |
| ------------------ | ------------------- | --------------------------------------------- |
| Mutable            | ✅ Yes               | ❌ No                                          |
| Syntax             | `[]`                | `()`                                          |
| Speed              | Slower              | Faster                                        |
| Use Case           | Flexible collection | Fixed, read-only data                         |
| Can be a dict key? | ❌ No                | ✅ Yes (if elements inside are also immutable) |

"""

people = [("Alice", 24), ("Bob", 30), ("Charlie", 22)]

for name, age in people:
    print(f"{name} is {age} years old.")

v = [(name,age) for name,age in people]
print(v)