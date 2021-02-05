# -*- coding: utf-8 -*-
import zohreh
import appendcategory
import input_apartment
import z
import pandas as pd
#responsible 
print("Hello. welcome")
while(1):
    inputs = input("if you want to append data please type 1 and if you want to get report type 2")
    if inputs==1:
        a=input('if you want to enter the date and time manually, enter 0 and otherwise enter 1: \n')
        time = zohreh.time(a)
        amount = int(input("enter the amount appended:\n"))
        category = appendcategory.category_input()
        responsible = input_apartment.apartment('Responsible Apartment')
##        related= [1,2,4,6,7]input("related")
        print("""enter the division method:
        1 Divided according to the number of inhabitants of each unit
        2 Divided by floor number
        3 Division according to the area of ​​each unit
        4 Divided by the number of parking spaces
        5 Divide evenly""")
        devisor= int(input())
        amountdevided = zohreh.f(z.g(d,related),amount,devisor)
        describtion = input("enter describtion:\n")
        data = {"Amount" : list(amountdevided.values()),
                "Time" : time,
                "Category" : category[0],
                "Subcategory" : category[1],
                "ResponsibeUnit" : responsible,
                "RelatedUnit" : list(amountdevided.keys()),
                "Describtion" : describtion}
        dataframe = pd.DataFrame(data)
        
        with open("data/accounts.csv", mode='a') as file:
            file.write(pd.DataFrame.to_csv(dataframe,index=False,line_terminator="\n"))
            
              
        
        
        
        