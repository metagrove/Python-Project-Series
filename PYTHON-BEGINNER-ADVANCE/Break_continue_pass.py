'''
break: exits the loop entirely

continue: skips current iteration

pass: placeholder for future code (does nothing)
'''

#
#
# def do_something():
#     pass  # To be implemented later
#
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     if i > 5:
#         break
#     print(i)
#

users = [
    {"username": "alice", "banned": False, "failed_logins": 1},
    {"username": "bob", "banned": True, "failed_logins": 0},
    {"username": "charlie", "banned": False, "failed_logins": 3},
    {"username": "dave", "banned": False, "failed_logins": 10},  # danger zone
    {"username": "eve", "banned": False, "failed_logins": 2},
]

print("Start processing users...\n")

for user in users:
    if user["banned"]:
        print(f"Skipping banned user: {user['username']}")
        continue  # go to the next user, skip everything below

    if user["failed_logins"] > 5:
        print(f"Too many failed logins for {user['username']}. Stopping system check!")
        break  # critical case: break out of loop completely

    print(f"Processing user: {user['username']}")
    print(f"  Failed logins: {user['failed_logins']}")
    print(f"  Status: OK\n")

print("\nUser processing complete.")
