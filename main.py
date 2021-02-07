# -*- coding: utf-8 -*-
import zohreh
import appendcategory
import input_apartment
import z
import pandas as pd
#responsible 
#zohreh start option from 1
#input_apartment add back option
print("Hello. welcome")
categories = ["Bill","Cleaning","Elevator","Parking","Repairment","Charge"]
subcategories = {"Bill":["Water","Electricity","Gas","Tax"]}
d={1:['id1',2,1,125,1],2:['id2',1,1,75,1],3:['id3',4,2,125,1],4:['id4',4,2,75,1],5:['id5',7,3,125,2],
   6:['id6',3,3,75,1],7:['id7',2,4,125,1],8:['id8',6,4,75,1],9:['id9',5,5,125,2],10:['id10',5,5,75,1]}

       
while(1):
    inputs = int(input("if you want to append data please type 1 and if you want to get report type 2 setting 3"))
    if inputs==1:
        n=0
        inputs={}
        while (n>=7):
            if n==0:  
                inputs[n]=input('if you want to enter the date and time manually, enter 0 and otherwise enter 1: \n')
                inputs["time"]= zohreh.time(inputs[n])
            if n==1:
                inputs["amount"] = int(input("enter the amount appended:\n"))
            if n==2:
                inputs["category"] = appendcategory.category_input(categories,subcategories)
            if n==3:
                inputs["subcategory"] = appendcategory.category_input(categories,subcategories,inputs["category"])
            if n==4:   
                inputs["responsible"] = input_apartment.apartment('Responsible Apartment')
            if n==5:
                related= [1,2,4,6,7]##input("related")
            if n==6:
                print("""enter the division method:
                      1 Divided according to the number of inhabitants of each unit
                      2 Divided by floor number
                      3 Division according to the area of ​​each unit
                      4 Divided by the number of parking spaces
                      5 Divide evenly
                      6 devided by default
                      0 Back""")
                inputs["devisor"] = int(input())
                if (inputs["devisor"] >=1 and inputs["devisor"] <= 7):
                    inputs["amountdevided"] = zohreh.f(z.g(d,inputs["related"]),inputs["amount"],inputs["devisor"])
                elif (inputs["devisor"] == 0):
                    inputs["devisor"] = "0"
                else: 
                    print("Wrong input please try again!")
                    continue
            if n==7:
                inputs["describtion"] = input("enter describtion:\n")
            if "0" in inputs.values():
                n -= 1
            else:
                n += 1
        data = {"Amount" : list(inputs["amountdevided"].values()),
                "Time" : inputs["time"],
                "Category" : inputs["category"],
                "Subcategory" : inputs["subcategory"],
                "ResponsibeUnit" : inputs["responsible"],
                "RelatedUnit" : list(inputs["amountdevided"].keys()),
                "TransactionAmount" : inputs["amount"],
                "Describtion" : inputs["describtion"]}
        dataframe = pd.DataFrame(data)
        
        with open("data/accounts.csv", mode='a') as file:
            file.write(pd.DataFrame.to_csv(dataframe,index=False,line_terminator="\n"))
            
              
        
        
        
        