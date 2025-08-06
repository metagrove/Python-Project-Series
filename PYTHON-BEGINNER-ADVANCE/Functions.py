'''

A function is a block of code that performs a specific task.
It helps you avoid repeating code, improves modularity,
and makes your code easier to test and maintain.

def: keyword to define a function

function_name: name you give to the function

parameters: optional values you pass to the function

return: sends a result back to the caller
'''

def new_func():
    print("Hello World")

new_func()

def do_somethiing():
    return "helo"
v = do_somethiing()
print(v)

def do_sometask(name,age):
    print(f"hi {name} you age is {age}!")

do_sometask("raj",22)

def do_something2(name):
    return f"helo {name}"
do_something2("yenn o")
print(do_something2("jerry"))