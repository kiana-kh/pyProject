# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:57:44 2021

@author: Asus
"""

a=input('Hi, if you want to enter the date and time manually, enter 0 and otherwise enter 1= ')

if a==0:
    Y=input('Enter the year=')
    M=input('Enter the month=')
    D=input('Enter the day=')
    C=input('Enter the clock=')
    m=input('Enter the minute=')
    S=input('Enter the Second=')
    date='{Year}-{Month}-{Day}- {Clock}:{Minute}:{Second}'.format(Year=Y,Month=M,Day=D,Clock=C,Minute=m,Second=S)
    print(date)

else:
    import datetime
    print(datetime.datetime.now())
###############################################################################
d={1:['id1',2,1,125,1],2:['id2',1,1,75,1],3:['id3',4,2,125,1],4:['id4',4,2,75,1],5:['id5',7,3,125,2],
   6:['id6',3,3,75,1],7:['id7',2,4,125,1],8:['id8',6,4,75,1],9:['id9',5,5,125,2],10:['id10',5,5,75,1]}
###############################################################################
'''
n=1 #Divided according to the number of inhabitants of each unit
n=2 #Divided by floor number
n=3 #Division according to the area of ​​each unit
n=4 #Divided by the number of parking spaces
n=5 #Divide evenly
'''
###############################################################################
def f(d:dict,Amount:float,n:int):
    a=0
    s={}
    for i in d:
        d[i].append(1)
    for i in d:
        a=a+d[i][n]
    b=Amount/a
    for i in d:
        s[i]={b*d[i][n]}
    return s
###############################################################################