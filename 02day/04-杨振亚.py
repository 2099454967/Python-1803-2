class Person():

	def sleep(self):
		print("睡觉")
	def eat(self):
		print("吃吃")
	def study(self):
		print("学习")
	def introduce(self):
		print("身高%d体重%d"%(self.height,self.weight))

yangzhenya = Person()
#当你调用上面这句话的时候,它会返回一个对象的引用，这个引用说白了就是self

#self就是谁调用方法就是指向谁
yangzhenya.sleep()#这不需要赋值 因为这是行为
yangzhenya.eat()
yangzhenya.study()
#下面这是属性
yangzhenya.height = 180
yangzhenya.weight = 80
yangzhenya.introduce()
