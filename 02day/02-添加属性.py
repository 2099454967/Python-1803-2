class Pig():
	
	def sleep(self):
		print("哼哼哼")

	def eat(self):
		print("猪饲料")
	
	def introduce(self):
		print("我叫%s年龄%d颜色%s"%(peiqi.name,peiqi.age,peiqi.color))
peiqi = Pig()#创建对象
peiqi.age = 12
peiqi.color = "粉色"
peiqi.name = "小猪佩奇"
peiqi.eat()#调用对象的方法
peiqi.sleep()#调用对象的方法
peiqi.introduce()#调用自我介绍
