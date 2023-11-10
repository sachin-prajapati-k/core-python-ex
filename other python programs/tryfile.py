number=int(input("enter the value"))
sq=1
r=number%10
sq=r*r
sumsq=sq
number=number//10
r=number%10
sq=r*r
number=number//10


print("sq",sumsq)
