'''the queue is a linear data structure.
   stores items in first in first out(fifo) manner.
'''
''' queue operation
        1. Enqueue: adds an item to the queue.
        2. Dequeue: removes an item from the queue.
        3. get the front item from queue.
        4.get the last item from queue.
'''
l=[]
while True:
    ch=int(input('''
        1. add element
        2. remove first element
        3. for view last element
        4. peek element
        5. display list
        6. exit
        '''))
    if ch==1:
        a=input("enter the value:- ")
        l.append(a)
        print(l)
    elif ch==2:
        if len(l)==0:
            print("list is empty")
        else:
            del l[0]
            print(l)
    elif ch==3:
        print("last element:",l[-1])
    elif ch==4:
        print("first element:",l[0])
    elif ch==5:
        print(l)
    elif ch==6:
        break;
    else:
        print("enter valid no.")
    
