import random
import string


def generator():
    length = int(input("Enter the length : "))
    in_uppercase = input("Yes or No").strip().lower()
    in_lowercase = input("Yes or No").strip().lower()
    in_digit = input("Yes or No").strip().lower()
    in_special_char = input("Yes or No").strip().lower()

    if length < 4:
        print("THE ENTRED LENGTH IS VERY LESS UNSECURED...")
        return
    
    upper = string.ascii_uppercase if in_uppercase == "yes" else ""
    lower = string.ascii_lowercase if in_lowercase == "yes" else ""
    digit = string.digits if in_digit =="yes" else ""
    spl_char = string.punctuation if in_special_char =="yes" else ""
    all_chars = upper+lower+digit+spl_char

    passwd = []
    if in_uppercase == "yes":
        passwd.append(random.choice(upper))
    if in_lowercase == "yes":
        passwd.append(random.choice(lower))
    if in_digit == "yes":
        passwd.append(random.choice(digit))
    if in_special_char == "yes":
        passwd.append(random.choice(spl_char))


    f_length = length - len(passwd)
    f_password = passwd

    for _ in range(f_length):
        chara = random.choice(all_chars)
        f_password.append(chara)
    random.shuffle(f_password)

    str_password  = "".join(f_password)
    return str_password

password = generator()
print(password)



"""
__________ANOTHER APPROCH___________


import random
import string

def generator():
    userlength = int(input("ENTER THE LENGTH : "))

    if userlength<4:
        print("NOT VALID LENGTH...")
        return
    
    gen_passwd = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    passwd = random.choices(gen_passwd,k=userlength)
    random.shuffle(passwd)
    str_pass = "".join(passwd)
    return str_pass

password = generator()
print(password)

"""



