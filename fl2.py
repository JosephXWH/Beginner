favourite_language = {
	'jacky':['python','go','r'],
	'cassy':['java','c','c++'],
	'judy':['pyhton','ruby'],
	'leo':['diff']
}
for name,languages in favourite_language.items():
 	if len(languages) > 1:
 		print(name.title() + " 's favourite language are")
 		for language in languages:
 			print("\t" + language.title())
 	else:
 		print(name.title() + " 's favourite language is")
 		for language in languages:
 			print("\t"+language.title())
