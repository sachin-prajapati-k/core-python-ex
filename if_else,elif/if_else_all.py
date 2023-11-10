n=int(input("enter the number "))
if n%2==0:
    print("the number is even")
else :
    print("the nubmer is odd")

print("number to find is it positive or negative or zero")

n=int(input("enter the number "))
if n>0:
    print("the number is positive")
else:
    if n==0:
        print("the number is zero")
    else :
        print (" the number is negative")

print("simple gross salary")

bs=int(input("enter the basic salary"))
if bs<20000:
    hra=bs*10/100
    da=bs*15/100
else:
    hra=bs*20/100
    da=bs*10/100
gs=bs+hra+da
print("gross salary is = ",gs)
    
