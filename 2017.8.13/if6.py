#coding=utf-8
import easygui
bb = float(easygui.enterbox("tell me how big your oil box is.s"))
hf = float(easygui.enterbox("告诉我油箱几成满。"))
mpk = float(easygui.enterbox("告诉我每单位油能走多远。"))

d = hf/10 * bb * mpk

if d >= 200:
	easygui.msgbox("油箱大小： " + str(bb)
		 + "pf" + str(hf)
		 + "KPL" + str(mpk)
		 +"fh13iouhfu2r[gh2uh45g[ui2hu4[gh2[")
else:
	easygui.msgbox("下车加油!")
