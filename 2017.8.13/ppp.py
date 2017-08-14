#coding=utf-8
import easygui 
import random

#初期的数值确定
a = 0
b = random.randint(1,100)
tries = 0

#前言
easygui.msgbox("""Hellow there, I am a guess number
	        robert,if you can guess the secret i keep, I will 
	        give you a surprice! """)

#当所猜测的数字不相同时
while a != b and tries < 6:
    a = int(easygui.enterbox("please enter your guess number"))
    if a > b:
    	easygui.msgbox("too high")
    elif a < b:
    	easygui.msgbox("too low")
    tries = tries+1

#当所猜测的数字相同时
if a == b:
	easygui.msgbox("conggratulations!")

#当次数用完时
else:
	easygui.msgbox("try next time!")
    
easygui.msgbox("The answer is " + str(b))
