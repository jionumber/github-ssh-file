#question 1

import datetime
now = datetime.datetime.now()
x = input("enter your name dear visitor:")
y = int(input("enter your age:"))
z = now.year - y
a = z + 100
print(a)

#question 2

x = int(input("enter any number :"))
if(x==0):
    print("wrong input")
elif(x%2==0):
    print("it is an even number.....")
else:
    print("it is an odd number....")




# question 6
x = str(input("enter any word :"))
rvs = x[::-1]
print(rvs)
if rvs == x:
    print("it is a palindrome number")
else:
    print("it is a non palindrome number")


#question 7

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2==0]
print(b)



#question 8
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
