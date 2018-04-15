def make_album(name, name_album, number=''):
	album = {'Artist':name,'Name of ab':name_album}
	if number:
		album['number'] = number
	return album
album = make_album("kris","cash")
print(album)
album1 = make_album("james","want to fire",8)
print(album1)
album2 = make_album("paris","fire your body",9)
print(album2)

	
