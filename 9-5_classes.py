class User():
    def __init__(self, first_name, last_name, age, location):
        self.fname = first_name
        # self.lname = last_name
        self.name = first_name + ' ' + last_name
        self.age = age
        self.loc = location
        self.login_attempts = 0

    def describe_user(self):
        print("The user named " + self.name.title() + " is "
              + str(self.age) + " years old and lives in "
              + self.loc.title())

    def greet_user(self):
        print("Hello, " + self.fname.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('alice', 'smith', 22, 'seattle')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("The user has logged in " + str(user1.login_attempts) + " times.")

user1.reset_login_attempts()
print("The user has logged in " + str(user1.login_attempts) + " times.")
