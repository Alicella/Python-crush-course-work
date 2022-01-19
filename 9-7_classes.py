class User():
    def __init__(self, first_name, last_name, age, location):
        self.fname = first_name
        # self.lname = last_name
        self.name = first_name + ' ' + last_name
        self.age = age
        self.loc = location

    def describe_user(self):
        print("The user named " + self.name.title() + " is "
              + str(self.age) + " years old and lives in "
              + self.loc.title())

    def greet_user(self):
        print("Hello, " + self.fname.title())


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


user1 = Admin('alice', 'smith', 22, 'seattle')

user1.describe_user()
user1.greet_user()

user1.privileges.privileges.append('invite new user')
user1.privileges.show_privileges()
