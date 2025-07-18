'''
input() reads a line of text from stdin.
It always returns a string, so conversion is needed for numeric input.
Crucial for interactive CLI apps.
'''

def get_number():
    while True:
        try:
           return int(input("Enter a number: "))
        except Exception as e:
            print("Error",e)

num = get_number()
print(num)
