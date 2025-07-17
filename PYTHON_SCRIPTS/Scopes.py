#L-E-G-B
'''
Local variables exist only inside functions

Global variables exist throughout the file
Use global keyword to modify a global variable
inside a function (generally discouraged in clean design).
'''
#Enclosing

var = "macc"
def cart():
    discount = 10
    def checkout():
        print(f"OFFER is applicable to user {var} discount of Rs:",discount)
    checkout()
cart()


#built in libs

count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1


