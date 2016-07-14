a=6                                #global

def local_func():          #global a is ot used in this func
    a=9                           #local
    print("local a=",a)
    return

print("global a=",a)
local_func()
#local_func(a)
