# class Shape:
#     def draw(self):
#         print("Drawing shape")

# class Circle(Shape):
#     def draw(self):
#         print("Drawing circle")

# class Square(Shape):
#     def draw(self):
#         print("Drawing square")

# # Usage
# shapes = [Circle(), Square()]

# for shape in shapes:
#     shape.draw()


# def greet() -> str:
#     return "helo"

# print(greet())


# def add(a:int,b:int)->int:
#     return a+b

# val = add(1,1)

# print(val)


def cal(x : int,y : int,user :str)->int:
    if user =="add":
        return x+y
    if user =="sub":
        return x-y
    if user =="mult":
        return x*y
    if user == "div":
        return x/y

    
a =int(input("ENTER A : "))
b =int(input("ENTER B : "))
usr_pref = input("ENTER MODE").strip().lower()
val = cal(a,b,usr_pref)
print(val)