from cumulativeaccounts import filteron_time
import pandas as pd

  
#number = [input('enter a number of floor=')]
#time1=input('enter first time=')
#time2=input('enter second time=')
#open the file
def financial_balance(dataframe,number,time1,time2):
    
    dataframe=dataframe[(dataframe['RelatedUnit'].isin(number))] 
    #dataframe['Time']=pd.to_datetime['Time']
    #dataframe= dataframe.sort_values(by='Time')
    dataframe=filteron_time(dataframe,(time1,time2))
    
    financialbalance = dataframe['Amount'].sum()
    return(financialbalance)

############################################

import datetime as datetime
def charge_estimate(dataframe):
    number=int(input('enter a number of floor='))
    dataframe=dataframe[(dataframe['RelatedUnit']== number)] 
    maxdates = dataframe['Time'].max()
    maxdates= datetime.date.fromisoformat(maxdates)
    records= maxdates - datetime.timedelta(days=365)
    dataframe=filteron_time(dataframe,(records.isoformat(),maxdates.isoformat()))
    summation=dataframe['Amount'].sum()
    chargeestimate=(summation/12)*1.2  ######### 20%نرخ تورم    
    return(number,int(chargeestimate))

