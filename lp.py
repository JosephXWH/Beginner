filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

text = ''
for line in lines:
	text += line.replace('In','His').strip()+ "\n"
print(text.rstrip())