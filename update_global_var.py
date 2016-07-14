a=9

def func():
    global a
    a=a+10
    print("inside a=",a)
    return

print("outside a=",a)
func()
print("after callin func -outside a=",a)
