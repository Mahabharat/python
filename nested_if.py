char=input()
if ord(char)>=65 and  ord(char)<=90:
    print("you have entered an UPPER case letter")
    if char in ('A','E','I','O','U'):
        print(char," is an alphabet")
    else:
        print(char," is an consonant")

elif  ord(char)>=97 and  ord(char)<=122:
    print("you have entered an lower case letter")
    if char in ['a','e','i','o','u']:
        print(char," is an alphabet")
    else:
        print(char," is an consonant")
else:
    print(char," is not an alphabet")
