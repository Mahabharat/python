#value
a=8
b=9
print("outside a and b=",a,"and",b)

def func(a,b):
    a+=10
    b+=10
    print("inside a and b=",a,"and",b)
    return

func(a,b)
print("after calling function outside a and b=",a,"and",b)


#reference
dictionary={'A':'Apple','B':'Ball','C':'Cat'}
print("outside dictionary",dictionary)

def func1(dictionary):
    new={'D':'Dog'}
    dictionary.update(new)
    print("inside dictionary",dictionary)
    return

func1(dictionary)
print("after calling function outside dictionary",dictionary)

#reference
list=[1,2,3]
print("outside list",list)

def func1(list):
    list.append(4)
    print("inside list",list)
    return

func1(list)
print("after calling function outside list",list)

#additional
dictionary={'A':'Apple','B':'Ball','C':'Cat'}       #global
print("outside dictionary",dictionary)

def func1(dictionary):
    #dictionary.clear()
    dictionary={'D':'Dog','E':'Egg'}                    #local....variable with same name
    print("inside dictionary",dictionary)               #global dictionary is never used
    return

func1(dictionary)
print("after calling function outside dictionary",dictionary)



