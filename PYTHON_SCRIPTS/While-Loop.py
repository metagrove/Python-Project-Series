'''
A while loop continues running as long as a condition is True.
Useful when the number of iterations isn’t known in advance.
'''

i = 0
# while i<10:
#     print(i)
#     i+=1

while True:
    password = input("CODE : ")
    if len(password)>8 and len(password) <10:
        print(password)
        print(password[:3]+"***"+password[-3])
        print("CREATED SUCCESSFULLY")
        print("YOU CAN LOGIN NOW ")
        break
    else:
        print("TRY AGAIN")