from random import randint

class die():
	def __init__(self,sides):
		self.sides = 10

	def roll_die(self):
		print(randint(1,self.sides))

my_die = die(10)
i = 1
while i<=10:
	my_die.roll_die() 
	i = i + 1
