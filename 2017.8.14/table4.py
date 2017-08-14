a = int(raw_input("Which nuber do you prefer to?"))
b = int(raw_input("How low do you want to go?"))
c = int(raw_input("How high do you want to go?"))
i = b
print ("Here your table.")
while b <= i <= c:
	print a,"*",i,"=",a*i
	i = i+1