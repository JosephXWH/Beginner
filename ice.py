class Restaurant():

	def __init__(self,name,typee,*number):
		self.name = name
		self.type = typee
		self.number = 0

	def describe_restaurant(self):
		state = self.type + ' ' + self.name  + ' ' +str(self.number) +" people in there!"
		return state.title()

	def open_restaurant(self):
		current_state = "THE RESTAURANT IS ON THE SALE!"
		print(current_state)

	def set_number_served(self):
		self.number = input("Please enter the peolpe in the kfc")

class Icecream(Restaurant):
	def __init__(self,name,typee,*number):
	 	super().__init__(name,typee,*number)
	 	self.flanors = ['choco','coffee','strawbery','orio']

	def show_the_flavor(self):
	 	for flavor in self.flanors:
	 		print("This icecream has this " + flavor.title() +" flavor.") 

my_favorite_resturant = Restaurant('kfc','fast food')
my_favorite_resturant.set_number_served()
print(my_favorite_resturant.describe_restaurant())
my_favorite_resturant.open_restaurant()
my_icecream = Icecream('doodoujump','coooooold',36)
my_icecream.show_the_flavor()
my_icecream.describe_restaurant()