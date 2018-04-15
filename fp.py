def make_shirt(apperance,size):
	print("Your T-shirt is " + apperance +", and size is " + size + ".")

def describe_city(name,belong_to):
	print(name.title() + " is in " + belong_to.title())

d_c = {'shanghai':'china','paris':'france','taiwan':'china'}
for lo,co in d_c.items():
	describe_city(lo,co)

make_shirt('I love Python','XXL')
make_shirt('I love Python','L')
make_shirt('Fuck Python','Oversize')
