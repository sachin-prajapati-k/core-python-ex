print("list 1")
l=[]
for a in range(1,100):
    l.append(a)
print(l)

print("list 2")
#with expression
n=[i for i in range(0,100,2)]
print(n)

print("list 3")
#with filter/ condition

m=[h for h in range(1,100) if h%2==0]
print(m)

#string convert to list
s="sachin"
k=[c for c in s]
print(k)

