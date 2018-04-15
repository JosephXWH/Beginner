filename = 'realpi.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.replace(' ','')

birthday = input("Please enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday is in the pi")
else:
	print("What a pitty.")
	
print(pi_string[:52] + "......")
print(len(pi_string))