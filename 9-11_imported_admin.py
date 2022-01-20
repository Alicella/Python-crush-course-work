import user_admin as ua

user1 = ua.Admin('alice', 'smith', 22, 'seattle')
user1.describe_user()
user1.greet_user()
user1.privileges.show_privileges()

user2 = ua.User('harry', 'jacob', 18, 'chicago')
user2.greet_user()
user2.describe_user()
