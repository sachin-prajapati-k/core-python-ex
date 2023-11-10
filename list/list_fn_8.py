#zip function of list
#it is used to iterate 2+ list or tuples
l=[10,20,30,40,50]
l2=[1,3,5,7,55,44]
for a,b in zip(l,l2):
    print(a,b)

print("other methode")

#other mehode to iterate 2+ string
l3=[20,40,60,80]
l4=[12,23,34,45]
l=len(l3)
for c in range(l):
    print(l3[c],l4[c])
