# -*- coding: utf-8 -*-
#should use comments properly
import pandas as pd
from pandas import DataFrame as df
def cumulative_input(data_dictionary: dict):
    """
    

    Parameters
    ----------
    data_dictionary : dict
        containing general information of all the available categories and building numbers.
    
    Description
    -----------
    Takes the factors for filtering on the data from user.
    (includes prompt text and minor exception handlings.)

    Returns
    -------
    filters_dictionary : dict
        dictionary with declared filtering factor.

    """
    #structur for filterby:" filterby (tuple of categories names in string format) (tuple of )
    first_level_prompt = "please enter the number of Filtering mode or type declared filtering structure: \n1.Based on categories\n"\
                         "2.based on building number\n3.based on dates\n"
    second_level_prompt = ["please enter desired categories in one line, separating them with space:",
                           "please enter desired building number in one line, separating them with space:",
                           "please enter desired time period with '/'. separate the dates with space:"]   
    ending_prompt=["You have choosen the following filters: ",
                   "categories of desired accounts: ",
                   "building numbers of desired accounts: ",
                   "time period which the accounts have taken place on: ",
                   "if you want to add or change a filter please enter 0. otherwise enter any character to continue:"]
    ##can be improved add help                   
    loop_break = "0"
    filters=["all categories","all building numbers","all times"]
    filters_dictionary:{"category": data_dictionary["categories"],
                        "number": data_dictionary["numbers"],
                        "date": ()}
            
    while (loop_break == "0"):
        ##takes input in two way and puts them in filters as strings
        try:
            inputs=[]
            inputs.extend(input(first_level_prompt).split())
            
            if  inputs[0] != "filterby":
                inputs.insert(1,input(second_level_prompt[int(inputs[0])-1]))
                filters[int(inputs[0])-1]=tuple(inputs[1].split())    
            elif inputs[0] == "filterby":
                for i in filters:
                    if type(i) != tuple:
                        raise TypeError("incorrect input")
                filters=[eval(i) for i in inputs[1:4]]##can be improved add except

            else:
                raise ValueError("incorrect input")
                
        except(ValueError,TypeError):
            print("the input does not match the defined structure/value. please try again.")
        finally:
            print("{t[0]}\n{t[1]}{f[0]}\n{t[2]}{f[1]}\n{t[3]}{f[2]}\n\n{t[4]}".format(t=ending_prompt,f=filters))##can be improved add until and..
            loop_break = input()
    #continue from here make filters_dictionary based on filters
    return filters_dictionary
              
                
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
def filteron_number(data,number: tuple):
    """
    
    Parameters
    ----------
    data : dataframe 
        containing accounts.
    number : tuple
        containing integers representing building numbers.
    
    Returns 
    -------
    newdf: dataframe
        containing filtered accounts 

    """           
        


def cumulative_filter(maindict:dict)
    with open("accounts.csv") as data:
    accounts = pd.read_csv(data)
    assigned_filters = cumulative_input(maindict)
    filtered_accounts = filteron_time(accounts,assigned_filters["date"])
    filtered_accounts = filteron_number(filtered_accounts, assigned_filters["number"])
    filtered_accounts = filteron_category(filtered_accounts, assigned_filters["category"])
    #df.groupby()

