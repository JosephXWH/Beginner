ask = "Please tell me what material do you want?"
ask += "\nWe will add it to your pizza."
while True:
	mater = input(ask)
	if mater == "quit":
		break
	
	print("we have add " + mater + " to your pizza.")
