def func(grades):
    first,*middle,last=grades
    print(first)
    print(middle)
    print(last)
    avg=sum(middle)/len(middle)
    print(avg)
    return
func([4,6,8,9,6,5])
