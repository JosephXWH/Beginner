#coding = utf-8
def charge_modle(unprinted_modles,complete_modles):
	while unprinted_modles:
		current_print =unprinted_modles.pop()
		print("Printing modle: " + current_print.title())
		complete_modles.append(current_print)

def show_com(finish):
	print("\nThat is the ptinted modle:")
	for fs in finish:
		print(fs.title()) 

upm = ['cat','pig','doom','angle']
cm = []

charge_modle(upm,cm)
show_com(cm)