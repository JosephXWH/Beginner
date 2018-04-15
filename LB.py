customers = ["GPJ","WJD","LST","XWH"]
print(customers)
#
the_guy_who_cannot_come = "LST"
customers.remove(the_guy_who_cannot_come)
print(customers)

#
customers.append("LZP")
print(customers)

#
customers.insert(2,"YPJ")
print(customers)

customers.sort()
print(customers)

for customer in customers:
	print(customer)

number=[value**3 for value in range(3,30,3)]
print number

k = number[2:4]
print k

#part_of_customers = customers[:3]
for part_of_customers in customers[:3]:
	print(part_of_customers.title()+" will come to the party this night.")

his_customers = customers[:]
print his_customers
his_customers.append("GHJ")
print his_customers

for customer in his_customers[:3]:
	print(customer.title() + " is a bad guy.")
print customers
print his_customers

#change the temple
size = (200,10)
print("original size = ")
for b in size:
	print b
print size[1]
size = (300,20,10)
print("later size = ")
for c in size:
	print c
print size[1]