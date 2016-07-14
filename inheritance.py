class parents():
	def last_name(self):
		print("Roberts")
	
class child(parents):
	def first_name(self):
		print("Paul")
		
	def last_name(self):		#override
		print("Bucky")
		
obj=child()
obj.last_name()
obj.first_name()
