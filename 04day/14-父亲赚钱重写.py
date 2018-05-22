class Father():

	def makemoney(self):
		print("双手赚钱")


class Son(Father):
	
	def makemoney(self):
		print("用脑子")
		super().makemoney()


nasiyuan = Son()
nasiyuan.makemoney()
	
