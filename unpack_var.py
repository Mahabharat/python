a,b,c=6,"uuu",'9'
print(a)
print(b)
print(c)

e,f,g=(6,"uuu",'9')
print(e)
print(f)
print(g)

u,v,w=[6,"uuu",'9']
print(u)
print(v)
print(w)

def unpackss(grades):
	
	*tuple=grades

	first, *tuple, last=grades
	print(first)
	print(tuple)
	print(last)
	avg=sum(tuple)/len(tuple)
	print(avg)

unpackss([5,7,9,8,7])
#unpack(6,8,8,9,7,6,5)
#unpack((5,6,4,6,5,7))
