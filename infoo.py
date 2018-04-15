def my_info(first,last,**other_info):
	profile = {}
	profile['first name'] = first
	profile['last name'] = last
	for key, value in other_info.items():
		profile[key] = value
	return profile

user_profile = my_info('xu','weihang',sex = 'male',hobby = 'play ball',mygirl = 'Lst')
print(user_profile)