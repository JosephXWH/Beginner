#coding=utf-8

class Car():

	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def get_describe_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

class ElectricCar(Car):
#初始化父类，super()用来连接父子两类的属性，后可加子类特有的属性，跟父类属性一致。
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery_size = 70
	
	def describe_battery(self):
		print("The battery size of this car is " + str(self.battery_size) + "-kWh battery")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 280
		print("This car can go approximately " + str(range) + " miles in full of " + str(self.battery_size) + "-kWh.")

class Battery():
	def __init__(self,size):
		self.size = size
	
	def upgrade_battery(self):
		if self.size == 85:
			print("There is no upgrade here!")
		else:
			self.size = 85
			print("85-kWh!!!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_describe_name())
my_tesla.describe_battery()
my_tesla.get_range()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_describe_name())

your_tesla = ElectricCar('dongfengqiya','Q6',2010)


