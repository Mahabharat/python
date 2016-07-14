import heapq

list=[44,78,90,5,34,76,89]
print(heapq.nlargest(3,list))

mylist=[
	{'ticket':'Guwahati','price':500},
	{'ticket':'Kochbihar','price':600},
	{'ticket':'Siliguri','price':900},
	{'ticket':'Tezpur','price':600},
	{'ticket':'Dibrugarh','price':1200}
	]

print(heapq.nsmallest(2,mylist, key=lambda mylist:mylist['price']))
print(heapq.nsmallest(2,mylist, key=lambda mylist:mylist['ticket']))
	
