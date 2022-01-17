def build_profile(first, second, **other_info):
    profile = {}
    profile['First Name'] = first.title()
    profile['Second Name'] = second.title()

    for key, value in other_info.items():
        profile[key.title()] = value.title()
    return profile

user_profile = build_profile('alice', 'chen', location = 'beijing', gender = 'female')
print(user_profile)