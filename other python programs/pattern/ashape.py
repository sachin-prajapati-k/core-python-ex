for j in range(1,6):
    for i in range(1,12):
        if(i>=j or i>=12-j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
