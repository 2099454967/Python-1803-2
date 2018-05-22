class Msg():
	
	#发送短信扣余额 #变成私有方法
	def __sendMsg(self,money):
		money -=1
		print("扣钱，发送短信")




msg = Msg()
msg.__sendMsg(-1)

