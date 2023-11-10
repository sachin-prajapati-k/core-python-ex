num=int(input("e t v"))
multiply=1
while(num>0):
    r=num%10
    multiply=multiply*r
    num=num//10
print(multiply)
