score = 0
coorectanswer = 9
timsanswer = 9

if timsanswer == coorectanswer:
   print "You did a good job!"
   score = score+1
print ("Thank you for playing!")
print ("Your score is " + str(score))

num1 = float (raw_input("Enter the first number!"))
num2 = float (raw_input("Enter your second number"))
if num1 > num2:
	print (num1, "is bigger than", num2)
if num1 < num2:
	print (num1, "is less than", num2)
if num1 == num2:
	print (num1, "is equal to", num2)
if num1 != num2:
	print (num1, "is not equal to", num2)
