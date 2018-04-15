responses = {}

poll_active = True
while poll_active:
	name = input("Hello,please tell me your name?")
	response = input("If you could visit one place in the world, where would you go? ")

	responses[name] = response

	active = input("Do you want to go ahead?(y/n)")
	if active == "n":
		poll_active = False

for name,response in responses.items():
	print(name.title() + " wants to go to " + response.title() + ".")


