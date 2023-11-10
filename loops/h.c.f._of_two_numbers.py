n1=int(input("enter the first no."))
n2=int(input("enter the second no."))
m=1
for i in range(1,n1+1):
    if n1%i==0  and n2%i==0:
        m=i
print("HCF of {} and {} is {}".format(n1,n2,m))
