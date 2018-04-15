def city_country(city_name,country_belong_to):
	print('"' + city_name + "," + country_belong_to + '"')
i = 0
while i<=3:
	a = input("Tell me your city!")
	b = input("Which does this city belong to?")
	city_country(a,b)
	i = i+1