class Enemy:
	life=3
	
	def attack(self):
		print("ouch!\n")
		#self.life-=1				#in self.var::separate object makes separate attack
		Enemy.life-=1				#in className.var::separate object makes same attack
	
	def check_life(self):
		if Enemy.life<=0:
		#if self.life<=0:
			print("You are dead\n")
		else:
			#print(str(self.life)+" lives left\n")
			print(str(Enemy.life)+" lives left\n")
			
			
object1=Enemy()
object1.attack()
object1.check_life()

object2=Enemy()
object2.attack()
object2.check_life()
