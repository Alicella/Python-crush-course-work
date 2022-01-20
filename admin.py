from userdef import User


class Privileges():
    def __init__(self, privileges=["add post", "delete post", "ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("The admin can " + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
