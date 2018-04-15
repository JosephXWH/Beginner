filename = 'guest2.txt'

with open(filename,'a') as file_object:
	i = 1 
	while i <= 6:
		c = input("Please enter the user name!")
		print("Hello! " + c.title())
		i = i + 1
		file_object.write(c + "\n")


	