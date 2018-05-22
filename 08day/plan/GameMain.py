import pygame
from PlanSprite import *

#1、敌机销毁轮播
#2、分数
#3、音乐


class PlaneGame(object):
	def __init__(self):
		
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)	
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		#定时器 毫秒
		#第一个参数是事件的名字
		#第二个参数是多长时间执行一次时间
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)


		pygame.time.set_timer(CREATE_BULLET_EVENT,500)

		#敌机的精灵组
		self.enemy_group = pygame.sprite.Group()


	def __create_sprites(self):
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)

		#创建英雄精灵
		
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)	
		
			

	def start_game(self):
		print("游戏开始...")
		while  True:
			self.clock.tick(FRAME_PER_SEC)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()	
		
	#事件处理
	def __event_handler(self):
		# pass
		
		for event in pygame.event.get():
		# 判断是否退出游戏
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:#定时器事件
				enemy = Enemy()
				self.enemy_group.add(enemy)
			elif event.type == CREATE_BULLET_EVENT:#子弹定时器事件
			
				self.hero.fire()

			# 获取用户按键
			keys_pressed = pygame.key.get_pressed()

			if keys_pressed[pygame.K_RIGHT]:
			    self.hero.speed = 2
			    self.hero.speed1 = 0
			elif keys_pressed[pygame.K_LEFT]:
			    self.hero.speed = -2
			    self.hero.speed1 = 0
			elif keys_pressed[pygame.K_UP]:
				self.hero.speed1 = -2
				self.hero.speed = 0
			elif keys_pressed[pygame.K_DOWN]:
				self.hero.speed1 = 2
				self.hero.speed = 0
			else:
				self.hero.speed1 = 0
				self.hero.speed = 0		



	def __check_collide(self):
		  # 1. 子弹摧毁敌机
		b = pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
		print(b)

	
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

		判断列表时候有内容
		if len(enemies) > 0:
			# 让英雄牺牲
			self.hero.kill()

			# 结束游戏
			PlaneGame.__game_over()
	
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)


		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		
		self.hero_group.update()
		self.hero_group.draw(self.screen)
		
		#
		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)
		

	@staticmethod		
	def game_over():
		pygame.quit
		exit()

if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()		
