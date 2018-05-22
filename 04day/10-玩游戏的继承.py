class Game():
	
	def play(self):
		print("玩游戏")	


class FPS(Game):
	
	def more_play(self):
		print("多人一起玩")


class Chiji(FPS):
	pass


huangye =Chiji()
huangye.play()
huangye.more_play() 	



