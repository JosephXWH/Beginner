import easygui

sex = easygui.choicebox("please tell us your sex.",
	          choices = ['male','female'])
age = easygui.enterbox("please enter your age")
if sex == "female" and 10 <= age <=12:
	easygui.msgbox("You could join in us")
else:
	easygui.msgbox("Sorry you cannot take this job.")