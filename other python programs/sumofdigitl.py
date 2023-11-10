number=int(input("enter the value of the number"))
sum=0
while(number>0):
    r=number%10
    sum=sum+r
    number=number//10
print(sum)
