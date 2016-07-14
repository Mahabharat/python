class ClassName:
    sample=0
    w=0
    b=0
    g=0
    o=0
    color_list=['white','black','green']

  #def __init__(self):
    def __init__(self, name):
        #print("Enter your name")                              #constructor, self arg is must in class
        #ClassName.nam=input()
        ClassName.nam=name                                #nam is a variable
        print("What is your colour?")
        ClassName.color=input()
        ClassName.sample+=1

    def check_color(self):
        if ClassName.color in ClassName.color_list:
            if ClassName.color ==ClassName.color_list[0]:
                ClassName.w=ClassName.w+1
            elif ClassName.color ==ClassName.color_list[1]:
                ClassName.b=ClassName.b+1
            else:
                ClassName.g=ClassName.g+1
        else:
            ClassName.o+=1

    def display(self):
        print("Your Name  is:", ClassName.nam)
        print("No of white colors=", ClassName.w)
        print("No of black colors=", ClassName.b)
        print("No of green colors=", ClassName.g)
        print("No of other colors=", ClassName.o)
        print("No of samples=", ClassName.sample)

'''
obj=ClassName("Ram")
obj.check_color()
obj.display()

obj1=ClassName("Shyam")
obj1.check_color()
obj1.display()

obj2=ClassName("Jadu")
obj2.check_color()
obj2.display()
'''

'''
for f in range(0,4):
    obj=ClassName()
    obj.check_color()
    obj.display()
'''

'''
name=["Ram","Shyam","Jadu"]
for f in range(0,3):
    obj=ClassName(name[f])
    obj.check_color()
    obj.display()
'''

'''
name=["Ram","Shyam","Jadu"]
f=0
while(f<3):
    obj=ClassName(name[f])
    obj.check_color()
    obj.display()
    f+=1
'''

j=0
names=[Ram, Shyam, Jodu, Modhu]
mylist=[]

while j<4:
	mylist.append(ClassName(names[j]))
	mylist[j].check_color()
	mylist[j].display()
	j+=1 
   

        
        
    
