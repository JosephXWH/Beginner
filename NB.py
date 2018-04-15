number = [1,4,6,89,76,43,45,77,22,80]
renumber = [3,5,7,2,9,43,78,77,80]
for num in renumber:
	if num in number:
		print("your number is " + str(num) + "we will push it to you.")
	else:
		print(str(num) + "is not required")
