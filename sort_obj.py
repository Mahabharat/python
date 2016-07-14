from operator import attrgetter

class User:
	def __init__(self, x, y):
		self.name=x
		self.user_id=y
	
	def __repr__(self):			#constructor for returning string
		return self.name+ " : " +str(self.user_id)
	
obj_list=[
	User('Bucky', 43),
	User('Sally', 5),
	User('Tuna', 61),
	User('Brian', 2),
	User('Joby', 77),
	User('Amanda', 9)
	]

print(sorted(obj_list))

for x in sorted(obj_list, key=attrgetter('name')):
	print(x)

print("_________________________________")
for x in sorted(obj_list, key=attrgetter('user_id')):
	print(x)
	

