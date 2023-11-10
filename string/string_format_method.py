#string format method

str="my name is {} prajapti i am {} year old".format("sachin",22)
print(str)

str2="my name is {0} prajapti i am {1} year old".format("sachin",22)
print(str2)

str3="my name is {1} prajapti i am {0} year old".format("sachin",22)
print(str3)

str4="my birth year is {y:10} and i am {a} year old".format(y=2000,a=22)#it gives the 10chr spaces before value
print(str4)

str5="my birth year is {y:^10} and i am {a} year old".format(y=2000,a=22) #it set the value between given spaces
print(str5)

str6="my birth year is {y:>10} and i am {a} year old".format(y=2000,a=22) # it gives the spaces before the value
print(str6)

str7="my birth year is {y:<10} and i am {a} year old".format(y=2000,a=22) # it gives the spaces after the value
print(str7)

