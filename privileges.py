class User():

	def __init__(self, first_name, last_name, age, sex, hobby):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.hobby = hobby		
		self.login_attempts = 0
	
	def describe_user(self):
		print(self.first_name.title() + " " + self.last_name + " " + " is a " + str(self.age) + " " + self.sex
			+ " whose hobby is " + self.hobby + ".")
		print(self.first_name.title() + " " + self.last_name + " has logged in for " + str(self.login_attempts)
			+ " times")

	def greet_user(self):
		print("Good morning " + self.first_name.title() + self.last_name.title())

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0 

class Admin(User):
	def __init__(self, first_name, last_name, age, sex, hobby):
		super().__init__(first_name, last_name, age, sex, hobby)
		self.privileges = ['can add post','can delete post','can ban user']

	def show_privileges(self):
		for pro in self.privileges:
			print("The admin " + pro + ".")

userone = User('lee','kang',18,'boy','playing football') 
usertwo = User('liu','lan',27,'girl','swimming')
userthree = User('jiang','xuehan',20,'girl','being a woman')
users = [userone,usertwo,userthree]
for user in users:
	if user.first_name ==  'lee':
		i = 0
		while i<= 3:
			user.increment_login_attempts()
			i += 1
	if user.first_name ==  'jiang':
		i = 0
		while i<= 100:
			user.increment_login_attempts()
			i += 1
	user.describe_user()
	user.greet_user()
	print("\t")
userthree.reset_login_attempts()
print(userthree.describe_user())

adminone = Admin('xu','weihang',20,'boy','playing computer games')
adminone.describe_user()
adminone.show_privileges()

