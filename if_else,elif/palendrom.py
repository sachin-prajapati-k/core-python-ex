num=int(input("enter the number"))
s=num
rev=0
r=0
r=num%10
rev=(rev*10)+r
num=num//10
r=num%10
rev=(rev*10)+r
num=num//10
r=num%10
rev=(rev*10)+r
if s==rev:
    print("the number is palendrom")
else:
    print("the number is not palendrom")
