class Msg():
	
	#发送短信扣余额 #变成私有方法
	#将来有些核心方法或者不想被别人直接调用，就可以写成私有方法
	def __sendMsg(self,money):
		money -=1
		print("扣钱，发送短信")

	def publicSend(self,money):
		if money <=0:
			print("发送失败")
		else:
			self.__sendMsg(money)


msg = Msg()
msg.publicSend(10)

