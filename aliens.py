aliens = []

for alien_number in range(30):
	new_alien = {'color':'green','points':15,'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[:6]:
	print(alien)
print("There are " + str(len(aliens)) + " aliens in this list")