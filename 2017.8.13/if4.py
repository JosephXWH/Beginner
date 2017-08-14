#coding=utf-8
import easygui

price = float (easygui.enterbox("请输入你心目中的价位。"))
if price <=10:
	lp = str(int(price*0.9))
	easygui.msgbox("你的折扣是九折，物品价格是" + lp)
else:
	dp =str(int(price*0.8))
	easygui.msgbox("你的折扣是八折，物品价格是" + dp)

"""在显示时，一定注意 types 是什么，否则常常出现不能显示的低级错误。"""