'''the stack is a linear data structure
    it store items in a Last-in/first-out(LIFO) or First-in/Last-
    Out(FILO) manner.
    stack operation
    1. push=> inserting an element
    2. pop => deletion an element(last element)
    3. peek=> desplay the last element
    4. display=> display list
    '''
l=[]
while True:
    ch=int(input('''
        1 for add element
        2 for pop(remove) element
        3 for peek(last) element
        4 for Display stack
        5 for exit program
        '''))
    if ch==1:
        n=input("enter the value :-")
        l.append(n)
        print(l)
    elif ch==2:
        if len(l)==0:
            print("stack is empty")
        else:
            pl=l.pop()
            print(pl)
            print(l)
    elif ch==3:
        if len(l)==0:
            print("empty stack")
        else:
            print("last stack value",l[-1])
    elif ch==4:
        print("display stack",l)
    elif ch==5:
        break;
    else:
        print("invalid choice")
        
