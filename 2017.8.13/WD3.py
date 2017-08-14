#coding=utf-8
import easygui
fahrenheittempreture = float(easygui.enterbox("""你那变多少华氏度啊？"""))
celsiustempreture = str(5.0/9*(fahrenheittempreture-32))
easygui.msgbox("哈哈哈，你内边贼垃圾，竟然" + celsiustempreture + "c")
