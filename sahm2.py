# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:36:20 2021

@author: Asus
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d= pd.read_excel( 'C:/Users/Asus/Desktop/data2.xlsx' )
def sahm1(d):
    Ghabz=0
    for i in range(len(d.index)):
        if d['daste'][i]=='Ghabz':
            Ghabz=Ghabz+int(d['mablagh'][i])
    water=0
    for i in range(len(d.index)):
        if d['zirdaste'][i]=='Water':
            water=water+int(d['mablagh'][i])
    bargh=0
    for i in range(len(d.index)):
        if d['zirdaste'][i]=='bargh':
            bargh=bargh+int(d['mablagh'][i])
    gaz=0
    for i in range(len(d.index)):
        if d['zirdaste'][i]=='gaz':
            gaz=gaz+int(d['mablagh'][i])
    avarez=0
    for i in range(len(d.index)):
        if d['zirdaste'][i]=='avarez':
            avarez=avarez+int(d['mablagh'][i])
            
    zirdastebandi=np.array(['water','bargh','gaz','avarez'])
    mablagh=np.array([water,bargh,gaz,avarez])


   
    font = {'family' : 'normal','size' : 14}
    plt.rc('font', **font)
    plt.xlabel('Mablagh')
    plt.ylabel('Ghabz')
    plt.barh(zirdastebandi[ np.argsort(mablagh)],np.sort(mablagh) )

    
    water=water/Ghabz
    bargh=bargh/Ghabz
    gaz=gaz/Ghabz
    avarez=avarez/Ghabz
    
    return(water,bargh,gaz,avarez)
    

def sahm2(d):
    a=list(set(d['daste']))
    Hazineh=0
    for i in range(len(d.index)):
        Hazineh=Hazineh+d['mablagh'][i]
    b=a.copy()
    for n in range(len(b)):
        b[n]=0
        for i in range(len(d.index)):
            if d['daste'][i]==a[n]:
               b[n]=b[n]+d['mablagh'][i]
    b=list(np.array(b)/Hazineh)
    
    # color for each label 
    colors = ['r', 'y', 'pink', 'g','skyblue','b'] 
    
    # plotting the pie chart 
    plt.pie(b, labels = a , colors=colors, 
    		startangle=90, shadow = True, explode = (0.1, 0.1, 0.1,0.1,0.1,0.1), 
    		radius =2, autopct = '%1.2f%%') 

    
    # showing the plot 
    plt.show() 
    
        
    return(np.array(a,b))