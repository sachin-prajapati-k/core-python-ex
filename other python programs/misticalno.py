number=int(input("enter the value of number"))
sum=0
pro=1
r=number%10
sum=sum+r
pro=pro*r
number=number//10
r=number%10
sum=sum+r
pro=pro*r
number=number//10
r=number%10
sum=sum+r
pro=pro*r
number=number//10
if(sum==pro):
    print("number is mistical")
else:
    print("number is not mistical")
