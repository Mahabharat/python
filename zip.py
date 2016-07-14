first=['Partha','Ritu','Udit']
middle=['Pritam','Raj','Narayana']
last=['Paul','Das','Bora']

name=zip(first,middle,last)
print(name)			#[('Partha','Pritam','Paul'),.....]
for a,b,c in name:
	print a,b,c
