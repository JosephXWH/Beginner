#coding=utf-8
import easygui

age = float(raw_input("please enter youe age."))
grade = float(raw_input("pplease enter your grade."))
if age >= 8:
	if grade >= 3:
		print("you can play with the real women.")
	else:
		print("go to study,baby.")
else:
	print ("go to bed ok?")
"""多重要求（即 if）下，若使用嵌套 if， 可反馈不同内容
   若使用 and 链接多个条件，则要求极高属于并列"""

height = float(easygui.enterbox("please enter your height."))
lofdick = float(easygui.enterbox("plaese enter your length of dick."))
if height >178 and lofdick<18:
    easygui.msgbox("oooooow,coool")
else:
    easygui.msgbox("getout") 
"""尝试将 if 语句和 gui 融合。。。。
   成功"""

age = float (raw_input("please enter youe age."))
grade = int (raw_input("please enter your grade."))
color = raw_input("please enter your favourite color.")
if age >= 8 and grade >= 3 and color == "green":
    print ("You can play this game boy.")
else:
	print ("This game is not suit for you.")
""" and 语句的条件很强硬，就像是串联，只要一处断连，就完全没办法通过。
    or 语句相比就要舒服很多，就像并联，有一处可通，就可以。"""

age = float (raw_input("please enter youe age."))
grade = int (raw_input("please enter your grade."))
color = raw_input("please enter your favourite color.")
if age >=8 or grade >=3 or color == "red" :
	print ("you could play this game already!")
else:
	print ("go to bed bro?")

age = float (raw_input("please enter youe age."))
if not ( age < 8):
	print ("You can play!")
else:
	print ("BED there!python")
