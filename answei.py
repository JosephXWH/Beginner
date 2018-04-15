filename = 'the_answer_why_learn_python.txt'

with open(filename,'a') as file_object:
	while True:
		answer = input("Why you learning the python programme?")
		if answer == "q":
			break
		file_object.write(answer + "\n")