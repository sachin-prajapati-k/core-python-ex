import pickle
file=open("first.txt","rb")
l=pickle.load(file)
print(l)
