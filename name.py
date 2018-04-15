def you_should_have_a_name(filename):

	try:
		with open(filename) as f_obj:
			names = f_obj.readlines()

	except FileNotFoundError:
		pass
		"""msg = "I can not find the file!"
		print(msg)"""

	else:
		if filename == "cats.txt":
			for name in names:
				print("This cats' name should be " + name.rstrip() + ".")
		
		elif filename == "dogs.txt":
			for name in names:
				print("This dog's name should be " + name.rstrip() + ".")

you_should_have_a_name('cats.txt')
you_should_have_a_name('dogs.txt')





		

		