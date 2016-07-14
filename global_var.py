a=12
def func1():
	print(a)
def func2():
	a=9				#local
	print(a)

def func3(a):
	a=8				#local
	print(a)
	

func1()
func2()
func3(a)

