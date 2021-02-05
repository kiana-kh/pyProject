from cumulativeaccounts import filteron_time
import pandas as pd

number=input('enter a number of floor=')
time1=input('enter fist time=')
time2=input('enter second time=')

#open the file
def financial_balance():
    d['time']=pd.to_datetime['time']
    d= d.sort_values(by='time')
    filteron_time(dataframe,(time1,time2))
    d=d[(d['number']== number)] 
    financialbalance = d.groupby('amount').sum()
    return(financialbalance)

############################################

import datetime as datetime
def charge_estimate():
    number=input('enter a number of floor=')
    d=d[(d['number']== number)] 
    maxdates=accounts['time'].max()
    maxdates= datetime.fromisoformat(maxdates)
    records=maxdates-timedelta(days=365)
    accounts=filteron_time(accounts,(maxdates.isoformat(),records.isoformat()))
    summation=accounts['Amount'].sum()
    chargeestimate=(summation/12)*1.2  ######### 20%نرخ تورم    
    return(chargeestimate)

