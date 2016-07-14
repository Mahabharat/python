def func(a,b=0,c=0):
	d=a*b+c
	print(d)
	
array=[2,3,4]

func(array[0],array[1],array[2])

func(*array)

func(array[0])

func(a=array[0],c=array[2])
