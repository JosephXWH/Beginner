#coding=utf-8
import easygui

ft = float(easygui.enterbox("""This is a tempreture convert system, you
should to enter the fahrenheit tempreture"""))
ct = int(5.0/9 * (ft-32))
easygui.msgbox("The celsius tempreture is " + str(ct) + " c")

"""int 和 float 不讲，需要灵活运用 str 将数
   值转化为字符串，才可在 msgbox 中呈现"""

"""还有一点就是对字符串（str），整数（int），和浮点数（float）
   需要多加了解!"""