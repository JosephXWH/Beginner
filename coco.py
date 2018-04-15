def counter(first_number,second_number):

	try:
		first_number = int(input("Please enter your first number: "))
		second_number = int(input("Please enter your second number: "))

	except ValueError:
		msg = ("Please enter the correct number!")
		print(msg)
	else:
		counter_number = first_number + second_number
		print(counter_number)
i = 1
while i <= 5:
	a = 0
	b = 0
	counter(a,b)
	i = i + 1


