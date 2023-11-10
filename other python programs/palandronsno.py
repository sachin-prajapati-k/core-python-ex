number=int(input("enter the value of the number"))
x=number
rev=0
r=number%10
rev=(rev*10)+r
number=number//10
r=number%10
rev=(rev*10)+r
number=number//10
r=number%10
rev=(rev*10)+r
number=number//10
if(x==rev):
    print("the number is palandrom")
else:
    print("the number is not palandrom")

