for i in range(1,6):
    for j in range(1,6):
        if i+j<=6:
            print(chr(j+64),end=" ")
        else:
            print(" ",end=" ")
    print("")
