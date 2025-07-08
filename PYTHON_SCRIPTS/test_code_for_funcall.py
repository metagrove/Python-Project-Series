# def add(a,b):
#     return a+b

def add(*args):
    total =0
    for num in args:
        total += num
    return total

def create_profile(**kwargs):
    print("------user profile-------")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
