current_number = 1
while current_number <=90909090:
	print(current_number)
	current_number *=7

prompt = "Tell me something i will repeat it to you."
prompt +="\nwhen you tell me quit we will quit\n"
message =""
while message != "quit":
	message = input(prompt)
	print("Do you like " + message + " this world?")
