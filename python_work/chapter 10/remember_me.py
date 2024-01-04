from pathlib import Path
import json

def get_stored_user_details(path):
    """Get stored user details if available."""
    if path.exists():
        contents = path.read_text()
        user_details = json.loads(contents)
        return user_details
    else:
        return None
    
def get_user_details():
    """Prompt for user details."""
    user_details = {}
    user_details["username"] = input("What is your name? ")
    user_details["gender"] = input("What is your gender? ")
    user_details["age"] = input("How old are you? ")

    path = Path("user_details.json")
    contents = json.dumps(user_details)
    path.write_text(contents)
    
    return user_details

def greet_user():
    """Greet the user by name with all their details."""
    path = Path("user_details.json")
    user_details = get_stored_user_details(path)

    if user_details:
        correctUser = input(f"Is {user_details} the correct user? (yes/no) ")

        if correctUser == "yes":
            print(f"Welcome back, {user_details}!")
        else:
            user_details = get_user_details()
            print(f"We'll remember you when you come back, {user_details}!")
    else:
        user_details = get_user_details()
        print(f"We'll remember you when you come back, {user_details}!")

greet_user()