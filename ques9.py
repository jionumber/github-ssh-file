
#question 9
import random
a = random.randint(1,9)
x = int(input("guess some number :"))
print(a)
if(x>a):
    print("your number is too greater")
elif(a==x):
    print("you guessed right")
else:
    print("your number is too small")

