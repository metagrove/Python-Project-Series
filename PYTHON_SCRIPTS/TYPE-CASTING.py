x = 10
print(type(x))

a = str(x)
#print(type(str(x)))
print(type(a))

# interger can be converted into string but string values cant be cnnverterd into integer or anytype
c = "a"
print(type(c))


x = "10.4"
print(type(x))
try:
    # q = int(x)
    q = float(x)
    print(type(q))

except Exception as e:
    print(e)









