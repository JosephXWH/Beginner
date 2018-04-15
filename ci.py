prompt = "\nTell me something i will repeat it to you."
prompt +="\nwhen you tell me quit we will quit\n"
while True:
	city = input(prompt)

	if city == "quit":
		break
	else:
		print("I'd love to go to " + city.title() + ".")