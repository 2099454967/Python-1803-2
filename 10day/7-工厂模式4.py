
class BmwStore(object):
	def order(self,type):
		return BmwFactory().selectCar(type)


class BCStore(object):
	def order(self,type):
		return BCFactory().selectCar(type)


class BCFactory(object):
	def selectCar(type):
		if type == 0:
			return Bmw730()
		elif type == 1:
			return Bmwx5()	

		
class BmwFactory(object):
	def selectCar(type):
		if type == 0:
			return DaG()
		elif type == 1:
			return XiaoG()			

class Car(object):
	def move(self):
		print("在移动")

	def music(self):
		print("播放音乐")	


class Bmw730(Car):
	pass


class Bmwx5(Car):
	pass


class DaG(Car):
	pass

class XiaoG(Car):
	pass	

if __name__ == '__main__':
	store = BmwStore()
	bmwx5 = store.order(1)
	bmwx5.move()
	bmwx5.music()	
	