#coding=utf-8
try:
	#11/0
	#open("xxx.txt")
	print(num)
	print("hahahahahhaha")
except (NameError,FileNotFoundError):
	print("出错了")
except Exception as ret:
	print("大错特错")
	print(ret)
else:
	print("没有错误会走这")
finally:
	print("有错没错都走")
print("hehehehehe")	
