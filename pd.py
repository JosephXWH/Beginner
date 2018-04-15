filename = 'Pussy_dick.txt'
filename2 = 'learning_python.txt'

with open(filename2,'r') as file_object2:
	lines = file_object2.readlines()

with open(filename,'w') as file_object:
	file_object.write("Please kiss my ass hole to make me feel goooood!!!")
	text = ""
	for line in lines:
		file_object.write(line.strip() + "\n")
