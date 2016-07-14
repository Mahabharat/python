for d in range(2,101):
    flag=True
    for e in range(2,d-1):
        if d%e is 0:
            print(d," is not a prime number")
            flag=False
            #break
        break
    if flag is True:
        print(d," is a prime number")
        
