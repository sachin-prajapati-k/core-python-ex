import pickle
l=[10,20,30,50]
file=open("first.txt","wb")
pickle.dump(l,file)
file.close()
