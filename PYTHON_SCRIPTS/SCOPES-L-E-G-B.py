#variable

def data():
    print("enclosing")
    var= 'Helo im enclosing '
    def msg():
        print(f"got inside {var} first and now inside msg function")
    msg()
data()


def data():
    food = "fried rice"
    print(food)
data()

print(__name__)

