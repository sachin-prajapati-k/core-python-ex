number=int(input("enter the number"))
sum=0
x=number
r=number%10
sum=sum+(r*r*r)
number=number//10
r=number%10
sum=sum+(r*r*r)
number=number//10
r=number%10
sum=sum+(r*r*r)
number=number//10
print(sum)
if(sum==x):
    print("the number is armstrong")
else:
    print("the number is not armstrong")
