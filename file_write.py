obj=open("ppp.txt",'w')
obj.write("Hello World!!")
obj.close()

obj=open("ppp.txt",'w')
obj.write("Gd mrnng guys")
obj.close()

obj=open("ppp.txt",'a')
obj.write("\nwhat's up?")
obj.close()

obj=open("ppp.txt",'r')
Str=obj.read()
print(Str)
obj.close()
