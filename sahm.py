# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:36:20 2021

@author: Asus
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def sahm1(d):
    Ghabz=0
    for i in range(len(d.index)):
        if d['Category'][i]=='Bills':
            Ghabz=Ghabz+int(d['Amount'][i])
    water=0
    for i in range(len(d.index)):
        if d['Subcategory'][i]=='Water':
            water=water+int(d['Amount'][i])
    bargh=0
    for i in range(len(d.index)):
        if d['Subcategory'][i]=='Electricity':
            bargh=bargh+int(d['Amount'][i])
    gaz=0
    for i in range(len(d.index)):
        if d['Subcategory'][i]=='Gas':
            gaz=gaz+int(d['Amount'][i])
    avarez=0
    for i in range(len(d.index)):
        if d['Subcategory'][i]=='Tax':
            avarez=avarez+int(d['Amount'][i])
            
    zirdastebandi=np.array(['Water','Electricity','Gas','Tax'])
    mablagh=np.array([water,bargh,gaz,avarez])


   
    font = {'family' : 'normal','size' : 14}
    plt.rc('font', **font)
    plt.xlabel('Amount')
    plt.ylabel('Bills')
    plt.barh(zirdastebandi[ np.argsort(Amount)],np.sort(Amount) )

    

    water=water/Ghabz
    bargh=bargh/Ghabz
    gaz=gaz/Ghabz
    avarez=avarez/Ghabz
    
    
    dictionary={"Water":water, "Electricity":bargh, "Gas":gaz, "Tax":avarez}
    return(dictionary)
    

def sahm2(d):
    a=list(set(d['Category']))
    Hazineh=0
    for i in range(len(d.index)):
        Hazineh=Hazineh+d['Amount'][i]
    b=a.copy()
    for n in range(len(b)):
        b[n]=0
        for i in range(len(d.index)):

            if d['Category'][i]==a[n]:
               b[n]=b[n]+d['Amount'][i]
    b=list(np.array(b)/Hazineh)
    
    # color for each label 
    colors = ['r', 'y', 'pink', 'g','skyblue','b','orchid'] 
    
    # plotting the pie chart 
    plt.pie(b, labels = a , colors=colors[:len(a)], 
    		startangle=90, shadow = True, explode = [0.1] * len(a), 
    		radius =2, autopct = '%1.2f%%') 

    # showing the plot 
    plt.show() 
    dictionary={}
    for i in len(a):
        dictionary[a[i]]= b[i]
        
    return(dictionary)


