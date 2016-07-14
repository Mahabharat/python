obj=open("paul.txt",'w')
obj.write("I love my India\n")
obj.write("Satyam Shivam Sundaram\n")
obj.close()

obj=open("paul.txt",'r')
text=obj.read()
print(text)
obj.close()
