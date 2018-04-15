class Airplane():

	def __init__(self,model,engine,wings,width,length,weight):
		self.model = model
		self.engine = engine
		self.wings = 2
		self.width = "30M"
		self.lenfth = "150M"
		self.weight = "2T"

	def take_off(self):
		print("The " + self.model + " is taking off.")

	def landing(self):
		print("The " + self.model + " is landing now.")

	def describe_airplane(self):
		print("The " + self.model + " has a " + self.engine + ",which has " + str(self.wings) +
			" is " + self.width +" width and " + self.lenfth +" long and " + self.weight +" weight.\tWhat's a plane")

my_Plane = Airplane('Boin747','nuclear',2,'30M','150M','2T')
take_off(my_Plane)

