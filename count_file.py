def count_word(filename):

	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exit."
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) +
			" words.")
books = ['The_Weird_Adventures.txt','The_Irish_Crisis.txt','Lanagan.txt']
for book in books:
	count_word(book)