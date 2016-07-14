list1=[23,34,45]

def func(i):
	return i*2
#1
k=0
dic={}	
for j in list1:
	dic[k]=func(j)
	k=k+1
print(dic[0])
print(dic[1])
print(dic[2])
print(dic.values())

#2
list2=list(map(func, list1))    #orlist2=map(func, list1)  
print(list2)

#3
mylist=[]
for k in list1:
	mylist.append(func(k))
	
print(mylist)
	
