current_users = ['amy', 'bob', 'charlie', 'dave', 'emily']
new_users = ['alex', 'brian', 'Dave', 'Emily', 'link']

for user in new_users:
	if user.lower() in current_users:
		print(user + ", Pls use another name.")
	else:
		print(user + ", Username available.")

