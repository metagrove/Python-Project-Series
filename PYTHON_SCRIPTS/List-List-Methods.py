# '''
# An ordered(index based access), mutable (changeable) collection.
#
# Can hold any data type: integers, strings, objects — even other lists.
#
# | Method          | What It Does                   | Example                     |
# | --------------- | ------------------------------ | --------------------------- |
# | `.append(x)`    | Add an item at the end         | `fruits.append("orange")`   |
# | `.insert(i, x)` | Insert at a position           | `fruits.insert(1, "grape")` |
# | `.remove(x)`    | Remove by value                | `fruits.remove("banana")`   |
# | `.pop(i)`       | Remove by index (last if none) | `fruits.pop()`              |
# | `.clear()`      | Empty the list                 | `fruits.clear()`            |
# | `.index(x)`     | Find position of value         | `fruits.index("apple")`     |
# | `.count(x)`     | Count occurrences              | `fruits.count("apple")`     |
#
# '''
#
# numbers = [1, 2, 3, 4, 5]
# mixed = [1, "hello", 3.14, True]
# empty = []
#
# def add_products():
#     count =0
#     while count<10:
#        prod = input("Enter product name : ")
#        empty.append(prod)
#        print(f"added product:{empty}")
#
# add_products()


mat =[[1,2],[3,4]]

# v = [col for row in mat for col in row]wha
# print(v)

for row in mat:
    for col in row:
        print([col])