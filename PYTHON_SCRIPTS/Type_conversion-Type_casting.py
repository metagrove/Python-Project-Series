'''
Convert types using functions like
int(), str(), float(). Check with type().

Like turning a toy car into a boat. You change what it is.

'''


num = "5"
print(int(num) + 2)  # Converts string to integer

x = 5
print(type(x))       # <class 'int'>
print(str(x))        # '5'

user_input = "123"
number = int(user_input)
print(number + 7)    # 130

data = ["1", "2", "3", "4.5", "bad"]

for item in data:
    try:
        num = float(item)
        print(f"{item} converted to {num}")
    except ValueError or Exception as e:
        print(f"{item} is not a number")


