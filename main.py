import time_and_category
import appendcategory
import ResAp
import project_f
import pandas as pd
import cumulativeaccounts
import json
import numpy as np
import percentage_numbers
import relatedunit
import name
import dataframe_to_csv
import sahm
import StatusColour
import status_f
print("Hello. welcome")
categories = ["Bills","Cleaning","Elevator","Parking","Repairment","Charge","Other"]
subcategories = {"Bills":["Water","Electricity","Gas","Tax"]}
intervals=(300000, 900000, 2000000)
directory="data/accounts.csv"
with open("data/Building.json","r") as data:
    BuildingData = json.load(data)
    
def append_manually(categories,subcategories, d):
    n=0
    inputs={}
    while (n<=7):
        if n == -1:
            break
        if n==0:  
            inputs[n]=input('if you want to enter the date and time manually, enter 1 and otherwise enter 2: \n')
            inputs["time"]= time_and_category.time(int(inputs[n])-1)
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
            inputs["responsible"] = ResAp.GetThecsvasDict()
        if n==5:
             inputs["related"] = relatedunit.append_relatedunit(BuildingData,int(input('if all units are relatedunit type 0,else type 1:  ')))
        if n==6:
            print("""enter the division method:
                  1 Divided according to the number of inhabitants of each unit
                  2 Divided by floor number
                  3 Division according to the area of each unit
                  4 Divided by the number of parking spaces
                  5 Divide evenly
                  6 devided by default
                  7 devide by percents
                  0 Back\n""")
            inputs["devisor"] = input()
            BuildingDataRelevent, inputs["All units"]  = name.filterunits(BuildingData,inputs["related"])
            if (int(inputs["devisor"]) >=1 and  int(inputs["devisor"]) <= 6):
                inputs["amountdevided"] = time_and_category.f(BuildingDataRelevent,int(inputs["amount"]),int(inputs["devisor"]),inputs["category"] + str(inputs["subcategory"]))
                inputs["amountdevided"] = list(inputs["amountdevided"].keys())
            elif (inputs["devisor"] == "7"):
                inputs["amountdevided"] = (np.array(percentage_numbers.percentage_input(BuildingDataRelevent)) * int(inputs["amount"]) /100).tolist()
            
            elif (inputs["devisor"] == "0"):
                pass
            else: 
                print("Wrong input please try again!")
                continue
        if n==7:
            inputs["describtion"] = input("enter describtion:\n")
        
        if "0" in inputs.values():
            #for Back commands
            n -= 1
            inputs.popitem()
            #needs python 3.7!
        elif "repeat" in inputs.values():
            continue
        else:
            n += 1
    
    
    if n == -1:
        return#going back to main window
    data = {"Amount" : inputs["amountdevided"],
            "Time" : inputs["time"],
            "Category" : inputs["category"],
            "Subcategory" : inputs["subcategory"],
            "ResponsibeUnit" : inputs["responsible"],
            "RelatedUnit" : inputs["related"],
            "TransactionAmount" : int(inputs["amount"]),
            "AllRelatedUnits" : str(inputs["All units"]),
            "Describtion" : inputs["describtion"]}
    dataframe = pd.DataFrame(data) 
    dataframe_to_csv.csvfile("0000-00-00","9999-99-99", dataframe, directory,False,"a")


def get_report(data,n):
    if n==1:
        #takes arguments
        number = [int(i) for i in input('enter unit numbers:\n').split()]
        time1=input('enter start date:(eg.1399-04-06)\n')
        time2=input('enter end date:(eg.1399-08-08)\n')
        project_f.financial_balance(BuildingData,number,time1,time2)
    if n==2:
        dataframe_to_csv.Getdatabetweentwodates(data)
    if n==3:
        options = {"expense portions of subcategories of Bills" : "1","expense portions of Categories" : "2"}
        select = ResAp.selectFromDict(options, "the portion report")
        if select=="1":
            print(sahm.sahm1(data))
        elif select=="2":
            print(sahm.sahm2(data))
    if n==4:
        cumulativeaccounts.cumulative_filter(data)
    if n==5:
        estimate=project_f.charge_estimate(accounts)
        print("Estimated charge per month of unit {} in next year is : {:,}".format(estimate[0],estimate[1]))

while(1):
    with open(directory) as data:
        accounts = pd.read_csv(data)
        balance = project_f.financial_balance(accounts,list(BuildingData.keys()),accounts['Time'].min(),accounts['Time'].max())
        status = status_f.get_status(intervals[0],intervals[1],intervals[2],balance)
    print("\n\n\n\nCurrent Status: " + str(status))
    selection_main = input("""please select: 
                          1 append data
                          2 report 
                          3 setting
                          4 exit\n""")
    if selection_main=="1":
        append_manually(categories, subcategories, BuildingData)
    if selection_main=="2":
        selection_report = input("""Please Choose:
                                 1 Balance Report
                                 2 Account File
                                 3 Portion Report
                                 4 Cumulative Expenses
                                 5 Charge Future Estimates
                                 0 Back\n""")
        get_report(accounts,int(selection_report))
        
    if selection_main=="3":
        options = {"Change Directory" : "1","Change Status intervals" : "2"}
        select_setting = ResAp.selectFromDict(options, "setting")
        if select_setting == "1":
            directory=input("enter The directory for appending and reporting:\n")
        elif select_setting == "2":
            intervals = StatusColour.StatusColours()
            
    if selection_main=="4":
        break
        
        
        
