num=int(input("enter the number"))
s=num
sum=0
r=0
r=num%10
sum=sum+r*r*r
num=num//10
r=num%10
sum=sum+r*r*r
num=num//10
r=num%10
sum=sum+r*r*r
if s==sum:
    print("the number is armstrong")
else:
    print("the number is not armstrong")
