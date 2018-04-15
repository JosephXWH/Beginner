filename = "The_Irish_Crisis.txt"

with open(filename,'r') as f_obj:
	lines = f_obj.read()

while True:
	word = input("Enter the word you want to count: ")
	if word == "quit":
		break
	word_number = lines.count(word)
	print(word_number)
	
