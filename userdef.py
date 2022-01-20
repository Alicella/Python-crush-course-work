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
