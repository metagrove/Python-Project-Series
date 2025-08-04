def add(*num):
    return sum(num)

number = (1,2,3,4,5,6)
print(add(*number))


def user_data(**kwargs):
    for key,values in kwargs.items():
        print(key, values)

user_data(name="john",age=20)

def full_info(title, *args, **kwargs):
    print(f"Title: {title}")
    print("Args:", args)
    print("Kwargs:", kwargs)

full_info("Report", 10, 20, author="Alice", pages=5)


def log_event(event, **details):
    print(f"Event: {event}")
    for k, v in details.items():
        print(f"{k}: {v}")

log_event("User Login", user="Alice", ip="192.168.0.1", device="mobile")
