import random as r
#随机数
i = r.randint(10,100)
print(i)
#文件的新用法
with open("1.txt",'w') as f:
	f.write("哈哈")
