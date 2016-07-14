bp=1600
sp=1500
if  bp<sp:
    print("congrats!")
    print("You have made a profit of",sp-bp,"bucks")
elif bp>sp:
    print("oops!")
    print("you have made a loss of",bp-sp,"bucks")
else:
    print("you  didn't make or loss money")
