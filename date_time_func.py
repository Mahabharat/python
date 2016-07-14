import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime())

tuple=(1995,8,26,15,26,15,1,250,0)
print(time.mktime(tuple))
print(time.localtime(time.mktime(tuple)))
time.sleep(7)
print("Hello World!!!")
