def make_car(name_of_producer,car_type,**other_info):
	profile = {}
	profile['Producer'] = name_of_producer
	profile['Type of the car'] = car_type
	for key, value in other_info.items():
		profile[key] = value
	return profile

car1 = make_car('subaru','outback',publicreview = 'very nice',old = '10 years')
car2 = make_car('dick','pussy',length = '10-inch')
car3 = make_car('sandwich','chocolate',py = 'dddpypy')
cars = [car1, car2, car3]
for car in cars:
	print(car)

