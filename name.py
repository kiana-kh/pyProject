<<<<<<< HEAD
# -*- coding: utf-8 -*-
def filterunits(data:dict,numberlist:list):
    newdata=data.copy()
    for e in list(data.keys()):
        if e not in numberlist:
            del newdata[e]
    name=[]
    for i in list(newdata.keys()):
        name.append(newdata[i][0])
    return newdata,name
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:12:26 2021

@author: Asus
"""
d={1:['id1',2,1,125,1],2:['id2',1,1,75,1],3:['id3',4,2,125,1],4:['id4',4,2,75,1],5:['id5',7,3,125,2],
   6:['id6',3,3,75,1],7:['id7',2,4,125,1],8:['id8',6,4,75,1],9:['id9',5,5,125,2],10:['id10',5,5,75,1]}

def g(d:dict,l:list):
    L=d.copy()
    for e in d.keys():
        if e not in l:
            del L[e]
    name=[]
    for i in L:
        name.append(L[i][0])
    return name
    
>>>>>>> 67d5fe619ce959e96e42cb748f03e48fe1434853
