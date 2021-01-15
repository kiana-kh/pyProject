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
        dictionary with declared filtering factor.

    """
    #structure for filterby:"filterby (tuple of categories names in string format) (tuple of desired unit numbers integers) (tuple of begining date and ending date with / and in string format)"
    #example:
    #filterby ("Elevator","Bills") (2,5,3,1) ("1399/03/24","1399/05/07") skip RelatedUnit
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
    filters=["all categories","all units","all times","RelatedUnit"]
    #1dropped idea 
    #1 filters_dictionary:{"categories": [False] + data_dictionary["categories"],
    #1                     "number": [False] + data_dictionary["numbers"],
    #1                     "date": [False]}
    
    while (loop_break == "0"):
        try:
            inputs=[]
            inputs.extend(input(first_level_prompt).split())
            
            if  inputs[0] != "filterby":
                inputs.insert(1,input(second_level_prompt[int(inputs[0])-1]))
                filters[int(inputs[0])-1]=tuple(inputs[1].split())    
            elif inputs[0] == "filterby":
                filters=[]
                for i in range(1,4):
                    inputs[i]=eval(inputs[i])
                    if type(inputs[i]) != tuple:
                        raise TypeError("incorrect input")
                filters= inputs[1:4]
                ##can be improved add except

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
        #can be improved add multiindex
    return filters
              
                
def filteron_time(data,time:tuple):
    """
    
    Parameters
    ----------
    data : dataframe 
        containing accounts.
    time : tuple
        containing two dates of datetime.date type.
    ----------
    
    Returns 
    -------
    newdf: dataframe
        containing filtered accounts 

    """
             
    
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
    newdf.reset_index(inplace=True)
    
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
    newdf.reset_index(inplace=True)
    
    return newdf        


#def cumulative_filter(maindict:dict):
    with open("accounts.csv") as data:
        accounts = pd.read_csv(data)
        assigned_filters = cumulative_input()
        filtered_accounts = accounts
        if assigned_filters[2] != "all times":
            filtered_accounts = filteron_time(filtered_accounts, assigned_filters[2])
        if assigned_filters[1] != "all units":
            filtered_accounts = filteron_unit(filtered_accounts, assigned_filters[1])
        if assigned_filters[0]  != "all categories":
            filtered_accounts = filteron_category(filtered_accounts, assigned_filters[0])
        #filtered_accounts.sort_values(inpalace=True)
        #filtered_accounts.set_index(["Category","RelatedUnit"],inplace=True)
        
