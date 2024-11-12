import random

n1=random.randrange(100)
maxtry=7
counter=0
while (counter<=maxtry):    
    userinput=int(input("guess the number"))
    if userinput==n1 and counter<=maxtry:
        print("congras you have won now you are gay:")
    elif userinput>n1 and counter<=maxtry:
        print("too high you have to go lower:")
    elif userinput<n1 and counter<=maxtry:
        print("too low you have to go higer:")
    counter=counter+1       

  