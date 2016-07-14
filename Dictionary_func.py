dictionary={'Apple':40,'Orange':50,'Banana':20,'Mango':45}
#first conver dictionary to list
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

list=zip(dictionary.keys(),dictionary.values())
print(list)
print(max(list))
print(min(list))
print(sorted(list))

list1=zip(dictionary.values(),dictionary.keys())
print(list1)
print(max(list1))
print(min(list1))
print(sorted(list1))


