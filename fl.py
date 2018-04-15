favourite_language = {
	'jacky':['python','go','r'],
	'cassy':['java','c','c++'],
	'judy':['pyhton','ruby']
}
for name in favourite_language.keys():
	for language in favourite_language.values():
		for item in language:
			print(name.title() + " 's favourite language is " + item + ".")
# There is a mistake!