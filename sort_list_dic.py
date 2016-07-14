from operator import itemgetter

users=[
	{'fname':'Bucky','lname':'Roberts'},
	{'fname':'Tom','lname':'Roberts'},
	{'fname':'Bernie','lname':'Zunks'},
	{'fname':'Jenna','lname':'Hayes'},
	{'fname':'Sally','lname':'Jones'},
	{'fname':'Amanda','lname':'Roberts'},
	{'fname':'Tom','lname':'Williams'},
	{'fname':'Dean','lname':'Hayes'},
	{'fname':'Bernie','lname':'Barbie'},
	{'fname':'Tom','lname':'Jones'},
	]
	
print(sorted(users, key=lambda users:users['fname']))

for x in sorted(users, key=lambda users:users['fname']):
	print x

print('\n')
for y in sorted(users, key=itemgetter('fname')):
	print y

print('-----')	
print('\n')
for z in sorted(users, key=itemgetter('lname')):
	print z
	
	
print('\n')
for u in sorted(users, key=itemgetter('fname','lname')):
	print u
	

	

