def make_album(name, name_album, number=''):
	album = {'Artist':name,'Name of ab':name_album}
	if number:
		album['number'] = number
	return album
while True:
	print("Tell me something about album!")
	print("Key in the q to quit the program")
	for_name = input("what's the name?")
	ab_name = input("What the name of the album?")
	num = input("How many songs in the album?")
	if num == 'q':
		break
	album = make_album(for_name,ab_name,num)
	print(album)
	