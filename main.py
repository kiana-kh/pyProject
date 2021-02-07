# -*- coding: utf-8 -*-
import zohreh
import appendcategory
import input_apartment
import z
import project_f
import pandas as pd
import cumulativeaccounts
#responsible 
#zohreh start option from 1
#input_apartment add back option
print("Hello. welcome")
categories = ["Bills","Cleaning","Elevator","Parking","Repairment","Charge"]
subcategories = {"Bills":["Water","Electricity","Gas","Tax"]}
d={1:['id1',2,1,125,1],2:['id2',1,1,75,1],3:['id3',4,2,125,1],4:['id4',4,2,75,1],5:['id5',7,3,125,2],
   6:['id6',3,3,75,1],7:['id7',2,4,125,1],8:['id8',6,4,75,1],9:['id9',5,5,125,2],10:['id10',5,5,75,1]}
len(d)
def append_manually(categories,subcategories, d):
    n=0
    inputs={}
    while (n<=7):
        if n == -1:
            break
        if n==0:  
            inputs[n]=input('if you want to enter the date and time manually, enter 1 and otherwise enter 2: \n')
            inputs["time"]= zohreh.time(int(inputs[n])-1)
        if n==1:
            inputs["amount"] = input("enter the amount appended:\n")
            if not (inputs["amount"].isnumeric()):
                print("wrong input.try again!")
                pass
        if n==2:
            inputs["category"] = appendcategory.category_input(categories,subcategories)
        if n==3:
            inputs["subcategory"] = appendcategory.subcategory_input(categories,subcategories,inputs["category"])
        if n==4:   
            inputs["responsible"] = input_apartment.apartment('Responsible Apartment')
        if n==5:
             inputs["related"]= [1,2,4,6,7]##input("related")
        if n==6:
            print("""enter the division method:
                  1 Divided according to the number of inhabitants of each unit
                  2 Divided by floor number
                  3 Division according to the area of ​​each unit
                  4 Divided by the number of parking spaces
                  5 Divide evenly
                  6 devided by default
                  0 Back\n""")
            inputs["devisor"] = input()
            if (int(inputs["devisor"]) >=1 and int(inputs["devisor"]) <= 7):
                inputs["amountdevided"] = zohreh.f(z.g(d,inputs["related"]),int(inputs["amount"]),int(inputs["devisor"]),inputs["category"] + str(inputs["subcategory"]))
            elif (inputs["devisor"] == "0"):
                pass
            else: 
                print("Wrong input please try again!")
                continue
        if n==7:
            inputs["describtion"] = input("enter describtion:\n")
        if "0" in inputs.values():
            n -= 1
            inputs.popitem()
            #needs python 3.7!
        elif "repeat" in inputs.values():
            continue
        else:
            n += 1
    if n == -1:
        return#going back to main window
    data = {"Amount" : list(inputs["amountdevided"].values()),
            "Time" : inputs["time"],
            "Category" : inputs["category"],
            "Subcategory" : inputs["subcategory"],
            "ResponsibeUnit" : inputs["responsible"],
            "RelatedUnit" : list(inputs["amountdevided"].keys()),
            "TransactionAmount" : int(inputs["amount"]),
            "Describtion" : inputs["describtion"]}
    dataframe = pd.DataFrame(data)
    


def get_report(data,n):
    if n==1:
        #im tired:(
        number = [int(i) for i in input('enter numbers of unit=\n').split()]
        time1=input('enter first time=')
        time2=input('enter second time=')
        project_f.financial_balance(dataframe,number,time1,time2)
    if n==1:
        pass
    if n==3:
        pass
    if n==4:
        cumulativeaccounts.cumulative_filter()
    if n==5:
        estimate=project_f.charge_estimate(accounts)
        print("Estimated charge per month of unit {} is : {:,}".format(estimate[0],estimate[1]))

while(1):
    with open("accounts.csv") as data:
        accounts = pd.read_csv(data)
        balance = project_f.financial_balance(accounts,list(d.keys()),accounts['Time'].min(),accounts['Time'].max())
        #status = get_status(balance,Green,Orange,Red)
    print("\n\n\n\nCurrent Status: " + str(balance))
    selection_main = input("""please select: 
                          1 append data
                          2 report 
                          3 setting
                          4 exit\n""")
    if selection_main=="1":
        append_manually(categories, subcategories, d)
    if selection_main=="2":
        selection_report = input("""Please Choose:
                                 1 Balance Report
                                 2 Account File
                                 3 Portion Report
                                 4 Cumulative Expenses
                                 5 Charge Future Estimates
                                 0 Back\n""")
        get_report(accounts,int(selection_report))
        
                  
              
        
        
        
        