sandwich_orders = ["tuna","sausager","pastrami","pastrami","hawaii","pastrami"]
finished_sandwiches = []

for peiliao in sandwich_orders:
	print("I made you " + peiliao + " sandwich.")
	finished_sandwiches.append(peiliao)

print("\nSorry pastrami sandwich has been sold out.")

while 'pastrami' in finished_sandwiches:
	finished_sandwiches.remove('pastrami')

while finished_sandwiches:
	print(finished_sandwiches)
	break
