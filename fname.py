def get_formatted_name(first_name,last_name):
	"""return the corract formatted name"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

def build_person(first_name,last_name,age=''):
	person = {'first' : first_name,'last':last_name}
	if age:
		person['age'] = age
	return person

muscian = get_formatted_name('jim','katter')
print(muscian)

phycist = build_person('kris','lee',age = 27)
print(phycist)
