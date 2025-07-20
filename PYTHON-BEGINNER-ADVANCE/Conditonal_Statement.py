'''
Conditional statements control the flow of code based on conditions.
Python uses:

if: for the first condition

elif: for more conditions

else: for fallback/default logic

Logical and comparison operators are often used here.

'''


def check_user_access(role):
    if role == "admin":
        return "Full Access"
    elif role == "editor":
        return "Edit Access"
    elif role == "viewer":
        return "Read-Only"
    else:
        return "No Access"

# print(check_user_access("editor"))
validate = check_user_access("admin")
print(validate)
