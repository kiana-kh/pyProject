from cumulativeaccounts import filteron_time
import pandas as pd

number=input('enter a number of floor=')
time1=input('enter fist time=')
time2=input('enter second time=')

#open the file

d.sort_values(by='time')
filteron_time(dataframe,(time1,time2))
d=d[(d['number']== number)] 
y=d.groupby('amount').sum()
print(y)

############################################

import datetime as datetime

number=input('enter a number of floor=')
d=d[(d['number']== number)] 
z=accounts['time'].max()
z= datetime.fromisoformat(z)
w=z-timedelta(days=365)
accounts=filteron_time(accounts,(z.isoformat(),w.isoformat()))
a=accounts['Amount'].sum()
b=(a/12)*1.2  ######### 20%نرخ تورم    
print(b)



