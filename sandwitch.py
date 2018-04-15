def sandwich_ing(*ingrediants):
	if len(ingrediants) == 1:
		print("This is the ingrediants of sandwitch: ")
		for ing in ingrediants:
			print(ing.title())
	else:
		print("There are the ingrediants of sandwitch: ")
		for ing in ingrediants:
			print(ing.title())

sandwich_ing('pig','tomato','potato','melon')
sandwich_ing('meet')
sandwich_ing('onian','garlic')
		
