class Mother():
	def last_name(self):
		print("Roberts")

class Father():
	def first_name(self):
		print("Paul")
		
class Child (Mother, Father):
	pass
	
obj=Child()
obj.last_name()
obj.first_name()
