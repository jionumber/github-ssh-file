
#question 11  
x = int(input("enter any number :"))
for i in range(2,x):
    if(x%i==0):
        print("it is not a prime number")
        break
else:
    print("it is a prime number")

