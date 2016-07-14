#class variable is default for any object
#instance variable is unique for that specific object
class girl:
	gender="female"			#class variable
	def __init__(self,name):
		self.name=name		#instance variable
		print(self.name)

r=girl("Sita")
print(r.gender)

s=girl("Gita")
print(s.gender)
