# usernames = []
usernames = ["jeff23", "jane450", "admin", "anon460", "fred49"]

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users")

print()
new_users = ["whoami", "jonny12", "ADMIN", "greg", "Fred49"]

for new_user in new_users:
    if new_user.lower() in usernames:
        print(f"{new_user} is not available. Please enter a unique username.")
    else:
        print(f"The username {new_user} is available.")

print()
ordinal_numbers = list(range(1, 10))

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print("1st")
    elif ordinal_number == 2:
        print("2nd")
    elif ordinal_number == 3:
        print("3rd")
    else:
        print(f"{ordinal_number}th")