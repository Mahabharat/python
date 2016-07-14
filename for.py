print("Enter your name")
name=input()
count=0

for l in name:
    if l in ['a','e','i','o','u']:
        count+=1
print("you have",count,"vowels in your name")
    
