# -*- coding: utf-8 -*-
#should use comments properly
#data_dictionary= {"numbers": [1,2,3,4,5,6],"categories": ["Bills","Elevator","Charge","Cleaning","Repairment"]}
#subcategory support must be implemented
#deal with nan in main program
import pandas as pd
from pandas import DataFrame as df

def cumulative_input():
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
    #example:       category         unit               dates                  index by
    #filterby Elevator,Bills:*Water,*Gas,Repairment 2,5,3,1 1399/03/24 1399/05/07 skip RelatedUnit
    first_level_prompt = "please enter the number of Filtering mode or type declared filtering structure: \n1.Based on categories\n"\
                         "2.based on building number\n3.based on dates\n"
    second_level_prompt = ["please enter desired categories in one line, separating them with space:\n",
                           "please enter desired building units in one line, separating them with space:\n",
                           "please enter desired time period with '/'. separate the dates with space:\n"]   
    ending_prompt=["You have choosen the following filters: ",
                   "categories of accounts that will be reported: ",
                   "building units whom the accounts refer to: ",
                   "time period which the accounts have taken place on: ",
                   "if you want to add or change a filter please enter 0. otherwise enter any character to continue:"]
    ##can be improved add help                   
    loop_break = "0"
    filters=["All categories","All units","All times","RelatedUnit"]
    
    while (loop_break == "0"):
        try:
            inputs=[]
            inputs.extend(input(first_level_prompt).split())
            
            if  inputs[0] != "filterby":
                #take input manually
                inputs.insert(1,input(second_level_prompt[int(inputs[0])-1]))
                filters[int(inputs[0])-1]=tuple(inputs[1].split())    
            elif inputs[0] == "filterby":
                #take input automatically
                filters=[]
                for i in range(1,5):
                    inputs[i]=tuple(inputs[i].split(","))
                filters= inputs[1:5]
                

            else:
                raise ValueError("incorrect input")
                
        except(ValueError,TypeError):
            print("the input does not match the defined structure/value. please try again.")
        if "skip" not in inputs :
            print("{t[0]}\n{t[1]}{f[0]}\n{t[2]}{f[1]}\n{t[3]}{f[2]}\n\n{t[4]}".format(t=ending_prompt,f=filters))##can be improved add until and..
            loop_break = input()
        else:
            break
    if "skip" not in inputs :
        base = int(input("choose which option to base the frame on it:\n1.Category\n2.Unit Number \n"))
        if base != 2:
            filters[3] = "Category" 
            
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
    int(time[0].replace("-",""))
    timeseries = accounts[["Time"]].str.replace("-","")
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
    
    newdf = data[data["Category"].isin(categories)]
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


def cumulative_filter(maindict:dict):
    with open("accounts.csv") as data:
        accounts = pd.read_csv(data)
    assigned_filters = cumulative_input()
    filtered_accounts = accounts.copy()
    if assigned_filters[2] != "All times":
        filtered_accounts = filteron_time(filtered_accounts, assigned_filters[2])
    if assigned_filters[1] != "All units":
        filtered_accounts = filteron_unit(filtered_accounts, assigned_filters[1])
    if assigned_filters[0]  != "All categories":
        filtered_accounts = filteron_category(filtered_accounts, assigned_filters[0])
    
    filtered_accounts.sort_values(by=[assigned_filters[3],"Time"],inplace=True)
    filtered_accounts = filtered_accounts[['RelatedUnit', 'Category', 'Amount', 'Time', 'Subcategory', 'ResponsibleUnit', 'Describtion'] ]
    cumulative_filter = filtered_accounts.groupby([assigned_filters[3]]).Amount.cumsum()
    filtered_accounts = filtered_accounts.join(cumulative_filter,rsuffix= (" cumulated by "+ assigned_filters[3]))
    filtered_accounts = filtered_accounts.join(filtered_accounts.Amount.cumsum(),rsuffix=" cumulated all")
    filtered_accounts.set_index(assigned_filters[3:],inplace=True)
    #print('{:*^40}'.format('Table'))
    