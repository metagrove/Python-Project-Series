'''
for loops are used to iterate over iterables like lists, strings, ranges, or dictionaries.
Python’s for is a high-level loop built on iter() and next().
'''

users = [{"name": "John"}, {"name": "Lily"}, {"name": "Sam"}]
print(users[0]['name'])

for user in users:
    pass

[user[0]['name'] for user in users if ['name']=='john']


#print(f"Hello, {user['name']}!")
x = [1,2,3,4,5,6,7,8,100]
print(["present" if i == 100 else "absent" for i in x])
v = ["p" if 100 in x else "AB"]
print(v)

t = sum(x for x in range(10) if x%2==0)
print(t)




