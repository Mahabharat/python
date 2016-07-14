try:
    print("Enter numerator")
    num=input()             #iit takes in input form
    print("Enter denominator")
    num1=input()
    res=int(num)/int(num1)
except:
    print("num1 can't be zero")
else:
    print("Result is:",res)
