num=int(input("enter the no."))
mul=1
sum=0
r=0
r=num%10
mul=mul*r
sum=sum+r
num=num//10
r=num%10
sum=sum+r
mul=mul*r
num=num//10
r=num%10
sum=sum+r
mul=mul*r
if sum==mul:
    print("the number is mistical")
else:
    print("the number is not mistical")
