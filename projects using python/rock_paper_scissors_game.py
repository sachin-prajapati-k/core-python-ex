import random as rd
l=['Rock','Scissors','Paper']
'''
rock vs paper     -> paper wins
rock vs scissor   -> rock wins
paper vs scissors -> scissors wins
'''
while True:
    ccount=0
    ucount=0
    uc=int(input('''
                Game Start......
                1 Yes
                2 No | Exit
                '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
            1 Rock
            2 Scissors
            3 Paper
            '''))
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice="scissors"
            elif userinput==3:
                uchoice="Paper"
            cchoice=rd.choice(l)
            if cchoice==uchoice:
                print("your choice : ",uchoice)
                print("computer choice : ",cchoice)
                ccount=ccount+1
                ucount=ucount+1
                print("Game Draw")
            elif (cchoice=="Rock" and uchoice=="Paper") or (uchoice=="Rock" and cchoice=="Scissors") or (cchoice=="Paper" and uchoice=="Scissors"):
                print("your choice : ",uchoice)
                print("computer choice : ",cchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("your choice : ",uchoice)
                print("computer choice : ",cchoice)
                print("computer Win")
                ccount=ccount+1
        if ucount==ccount:
            print('''
            Game Final
            Both Are Winner''')
        elif ucount>ccount:
            print("You Win The Game")
        else:
            print("Computer Win The Game")
    else:
        break;

























