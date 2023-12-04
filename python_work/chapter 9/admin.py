from user import User

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, occupation: str, privileges: []):
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = privileges

    def show_privileges(self):
        print("List of user privileges: ")
        for privilege in self.privileges:
            print(privilege)

print()
user = Admin("Jarryd", "Deane", 31, "Software Engineer", ["can add post", "can delete post", "can ban user"])
user.show_privileges()
    