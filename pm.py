#coding=utf-8
"""创建两个列表，其中一个包含要处理的数据"""
unprinted_modles = ['dodecahdron','robot pendant','iphone case']
complete_modles = []

"""模拟打印，知道没有未打印的为止"""
"""将打印完成的移入完成列表"""
while unprinted_modles:
	current_design = unprinted_modles.pop()

	"""模拟打印过程"""
	print("Printing modle: " + current_design)
	complete_modles.append(current_design)

"""显示打印好的所有类型"""
print("\nThe folling modles have been printed:")
for complete_modle in complete_modles:
	print(complete_modle)