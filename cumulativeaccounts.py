
# -*- coding: utf-8 -*-


import pandas as pd
from pandas import DataFrame as df
import matplotlib
import matplotlib.pyplot as plt
import  ResAp
import numpy as np
def cathandle(x):
    #creates a column showing both category and subcategory if that makes it nan only category is shown 
    if np.isnan(x["Subcategory"]):
        return x["Category"]
    else:
        return x['Category'] + ":" + x["Subcategory"]
def exspenseflow_input():
    """
    
    Description
    -----------
    Takes the factors for filtering on the data from user.
    (includes prompt text and minor exception handlings.)

    Returns
    -------
    filters_dictionary : dict
        dictionary with filtering factor.

    """
    #structure for filterby:"filterby (tuple of categories names in string format) (tuple of desired unit numbers integers) (tuple of begining date and ending date with / and in string format)"
    #example:       category                        unit           dates                  index by
    #filterby Elevator,Bills:*Water*Gas,Repairment 2,5,3,1 1399-03-05,1400-01-01 skip RelatedUnit
    first_level_prompt = "please enter the number of Filtering mode or type declared filtering structure: \n1.Based on categories\n"\
                         "2.based on building number\n3.based on dates\n"
    second_level_prompt = ["please enter desired categories in one line, separating them with space:\n(eg.Elevator Bills:*Water*Gas)\n",
                           "please enter desired building units in one line, separating them with space:\n(eg.1 2 3)\n",
                           "please enter desired time period with '-'. separate the dates with space:\n(eg.1399-04-05 1399-05-05)\n"]   
    ending_prompt=["You have choosen the following filters: ",
                   "categories of accounts that will be reported: ",
                   "building units whom the accounts refer to: ",
                   "time period which the accounts have taken place on: ",
                   "if you want to add or change a filter please enter 0. otherwise enter any character to continue:"]
                  
    loop_break = "0"
    filters=[["Allcategories"],["Allunits"],["Alltimes"],"RelatedUnit"]
    
    while (loop_break == "0"):
        try:
            inputs=[]
            inputs.extend(input("_"*30 +"\n" +first_level_prompt).split(" "))
        
            if inputs[0] == "filterby":
                #take input automatically
                filters=[]
                for i in range(1,4):
                    inputs[i]=inputs[i].split(",")
                filters= inputs[1:4]
            elif  int(inputs[0])>=0 and int(inputs[0])<=3:
                #take input manually
                inputs.insert(1,input(second_level_prompt[int(inputs[0])-1]))
                filters[int(inputs[0])-1]=inputs[1].split()
            

            else:
                raise ValueError("incorrect input")
                
        except(ValueError,TypeError,IndexError):
            print("the input does not match the defined structure/value. please try again.")
            
        #prints report    
        if "skip" not in inputs :
            print("_"*30 + "\n\n{t[0]}\n{t[1]}{f[0]}\n{t[2]}{f[1]}\n{t[3]}{f[2]}\n\n{t[4]}".format(t=ending_prompt,f=filters))
            loop_break = input()
        else:
            break
    if ["Allcategories"] != filters[0]:
        for i in range(len(filters[0])):
            # makes subcategories a sole item of list  
            if "*" in filters[0][i]:
                filters[0].extend(filters[0][i][filters[0][i].find(":")+2:].split("*"))
                filters[0][i] = filters[0][i][:filters[0][i].find(":")]
                filters[0]=[element.title() for element in filters[0]]
        #makes first letter capital
        filters[0]=[element.title() for element in filters[0]]
        
    if "skip" not in inputs :
        options={"Based on diffrent Category":"Category","Based on diffrent Units": "RelatedUnit","Show all building expenses flow":"All"}
        filters.insert(3,ResAp.selectFromDict(options, "the method for plotting")  )      
    else:
        filters.append(inputs[5])
    
    return filters
              
                
def filteron_time(data,timelimit:tuple):
    """
    
    Parameters
    ----------
    data : dataframe 
        containing accounts.
    time : tuple
        containing two dates of string type.
    ----------
    
    Returns 
    -------
    newdf: dataframe
        containing filtered accounts 

    """
    #timelimit=("1399-04-15","1399-06-10")
    timeseries = data["Time"].str.replace("-","")
    timeseries= pd.to_numeric(timeseries)
    data= data[(timeseries >= int(timelimit[0].replace("-",""))) & (timeseries <= int(timelimit[1].replace("-","")))]
    return data

def filteron_category(data,categories: tuple):
    """
    
    Parameters
    ----------
    data : dataframe 
        containing accounts.
    category : tuple
        containing strings of category names.
    
    Returns 
    -------
    newdf: dataframe
        containing filtered accounts 

    """
    booleancategory = data["Category"].isin(categories) & (data["Subcategory"].isna() | data["Subcategory"].isin(categories))
    newdf = data[booleancategory]
    newdf.reset_index(inplace=True,drop=True)
    
    return newdf

          
def filteron_unit(data,number: tuple):
    """
    
    Parameters
    ----------
    data : dataframe 
        containing accounts.
    number : tuple
        containing integers representing unit numbers.
    
    Returns 
    -------
    newdf: dataframe
        containing filtered accounts 

    """        
    newdf = data[data["RelatedUnit"].isin(number)]
    newdf.reset_index(inplace=True,drop=True)
    
    return newdf        


def cumulative_filter(accounts):
    accounts = accounts[accounts["Category"] != "Charge"]
    assigned_filters = exspenseflow_input()
    filtered_accounts = accounts.copy()
    
    if assigned_filters[2] != ["Alltimes"]:
        filtered_accounts = filteron_time(filtered_accounts,( assigned_filters[2][0], assigned_filters[2][1]))
    if assigned_filters[1] != ["Allunits"]:
        filtered_accounts = filteron_unit(filtered_accounts, assigned_filters[1])
    if assigned_filters[0]  != ["Allcategories"]:
        filtered_accounts = filteron_category(filtered_accounts, assigned_filters[0])
    
    filtered_accounts.sort_values(by=["Time"],inplace=True)

    y_values={}
    if (assigned_filters[3] != "All"):
        if (assigned_filters[3] == "Category"):
            filtered_accounts["CatandSub"]=(filtered_accounts["Category"] +":" +filtered_accounts["Subcategory"]).fillna(filtered_accounts["Category"])
            assigned_filters[3]="CatandSub"
        #calculates cumulative sum based on filter and puts it in dataframe
        cumulative_filter = filtered_accounts.groupby([assigned_filters[3]]).Amount.cumsum()
        filtered_accounts = filtered_accounts.join(cumulative_filter,rsuffix= (" cumulated by "+ assigned_filters[3]))
        #creates cumulative values for each category/unit to use in y axis
        for i in set(filtered_accounts[assigned_filters[3]]):
            y_values[i]=filtered_accounts[filtered_accounts[assigned_filters[3]] == i][["Time","Amount cumulated by "+ assigned_filters[3]]]
    else:
        #calculates all accounts cumulative value
        filtered_accounts = filtered_accounts.join(filtered_accounts.Amount.cumsum(),rsuffix=" cumulated by All")
        y_values["All"]=filtered_accounts[["Time","Amount cumulated by "+ assigned_filters[3]]]
    

    fig = plt.figure(figsize=(12,8))
    plt.xticks(rotation=70)
    for i in y_values:
        #fix dates and createsplot
        plt.plot( y_values[i]["Time"], y_values[i]["Amount cumulated by "+ assigned_filters[3]],label=i,marker=".")
    ax = plt.axes()
    ax.xaxis.set_major_locator(plt.MaxNLocator(15))
    plt.legend()
    print("do you want to save the plot?(True/False)")
    plt.show()
    t=bool(input())
    if t:
        fig.savefig("user/plot.png")

