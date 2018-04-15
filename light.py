class Light():

	def __init__(self):
		self.electricity_power = True
		self.light_statue = True
		self.c_solar_power = False
		self.u_solar_power = False
		self.the_time = 0

	def turn_on_the_light(self):
		self.light_statue = True 

	def turn_down_the_light(self):
		self.light_statue = False

	def collect_the_solar_power(self):
		self.electricity_power = False
		self.c_solar_power = True

	def use_the_solar_power(self):
		self.u_solar_power = True

	def use_the_electricity_power(self):
		self.solar_power = False
		self.electricity_power = True

	def power_time_caculate(self):
		if self.the_time >= 7:
			self.collect_the_solar_power()
		if self.the_time >= 19:
			self.use_the_electricity_power()
			self.use_the_solar_power()
			self.c_solar_power = False

	def off_time_caculate(self):
		if self.the_time >= 7:
			self.turn_down_the_light()
		if self.the_time >= 19:
			self.turn_on_the_light()

print("There's a light that combines the e and s power to light!\nLet's take a look!\n")
light1 = Light()
i = 0
while i <= 24:
	print("Now is the " + str(light1.the_time) + " o'clock.")  
	light1.the_time += 1
	light1.power_time_caculate()
	light1.off_time_caculate()
	print("Is that collecting solar power?" + str(light1.c_solar_power))
	print("Is that solar power? " + str(light1.u_solar_power))
	print("Is that electricity power? " + str(light1.electricity_power))
	print("Is that light on? " + str(light1.light_statue))
	print("\t")
	i += 1








