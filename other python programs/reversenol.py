num=int(input("e t v "))
rev=0
while(rev>0):
    r=num%10
    rev=(rev*r)+r
    num=num//10
print(rev)
