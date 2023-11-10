#datetime module in python
import datetime as dt
x=dt.datetime.now()
print(x)
'''
    the date contains year,month,day,hour,minute,second,and
    microsecond.
    '''
#creating date objects
x=dt.datetime(2023,2,22)
print(x)
 
'''
    he method is called strftime(), and takes one parameter,
    format,to specify the format of the returned string:
    %b   month name,short version  i.e. Dec
    %B   month name,full version   i.e. December
    %m   month as a number 01-02   i.e. 12
    %y   year, short version, without century i.e. 18
    %Y   year,full version         i.e. 2018
    %H   hour 00-23                i.e. 17
    %i   hour 00-12                i.e. 05
    %p   AM/PM                     i.e. PM
    %M   Minute 00-59              i.e. 41
    '''
z=dt.datetime.now()
y=z.strftime("%y")
print(z)
print(y)
Y=z.strftime("%Y")
print(Y)
m=z.strftime("%b")
print(m)
M=z.strftime("%B")
print(M)
mn=z.strftime("%m")
H=z.strftime("%H")
print(H)
I=z.strftime("%I")
print(I)
p=z.strftime("%p")
print(p)
mi=z.strftime("%M")
print(mi)
















