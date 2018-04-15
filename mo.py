responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat's your name.")
	response = input("Which mountain do you want to go this weekend?")

	responses[name] = response

	repeat = input("Do you want to contionue polling?(y/n)")

	if repeat == "n":
		polling_active = False

for name,response in responses.items():
	print("\n" + name.title() + " wants to go to " + response.title())