#人类
class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None

	def zhuangzidan(self,danjia,bullet):
		danjia.addBullet(bullet)

	def zhuangdanjia(self,gun,danjia):
		gun.addDanJia(danjia)

	def takeGun(self,gun):#老王拿枪
		self.gun = gun


#枪类
class Gun():
	def __init__(self,name):
		self.name = name
		self.danjia = None
	#装弹夹
	def addDanJia(self,danjia):
		self.danjia = danjia
		print(id(self.danjia))
#弹夹
class DanJia():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []
	
	def addBullet(self,bullet):
		self.bullet_list.append(bullet)
		print(len(self.bullet_list))	
#子弹
class Bullet():
	pass



laowang = Person("老王")
ak47 = Gun("ak47")
danjia = DanJia(20)#可以放20颗子弹
for i in range(20):
	bullet = Bullet()
	laowang.zhuangzidan(danjia,bullet)#装子弹
laowang.zhuangdanjia(ak47,danjia)#装弹夹

laosong = Person("老宋")#创建一个人
laowang.takeGun(ak47)#老王拿枪
