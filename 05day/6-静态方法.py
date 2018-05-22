class Game():
	count = 0	
	def play(self):#实例方法
		print("玩游戏----实例方法")

	@classmethod  #类方法
	def show(cls):
		print("展示-----类方法")

	@staticmethod
	def menu():
		print("1、开始游戏")
		print("2、结束游戏")


wangzhe = Game()#实例对象
wangzhe.play()#调用实例方法

Game.show() #通过类调用类方法
wangzhe.show()#通过对象调用类方法

Game.menu()#通过类调用静态方法
wangzhe.menu()#通过对象调用静态方法

	
