class Game(object):
		
	#执行下面方法的时候一定拥有了对象
	#下面的参数self到底是谁给他的？
	def __init__(self):
		self.name = "哈哈"

	
	def __new__(cls):
		
		return object.__new__(cls)	
		
	
		





chiji = Game()
#上面这句话是创建实例对象，但是你们怎么知道的创建的

#创建实例化对象的时候步骤
#调用new方法 返回对象的引用
#把引用给init方法
#调用init

