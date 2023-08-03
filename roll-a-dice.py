import random

no=random.randint(1,6)
print("press y to roll and n to exit!")
response=input("Will you roll a dice??")
if(response=='y'):
    print(no)
elif(response=="n"):
    print("Thanks for rolling the dice!")