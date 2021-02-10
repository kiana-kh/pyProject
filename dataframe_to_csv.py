import cumulativeaccounts
def csvfile(startdate,enddate, df, name,bheader,smode):
    import pandas as pd
    df = cumulativeaccounts.filteron_time(df,(startdate,enddate))
    df.to_csv(name,header=bheader,mode=smode)

def Getdatabetweentwodates(df): 
    print("Enter the Required Dates in this form: 2000-06-02")
    startdate = str(input("Enter the Start Date:"))
    enddate = str(input("Enter the End Date:"))
    filename = 'user/' + ('Report Between {} and {}.csv'.format(startdate,enddate))
    bheader = True
    csvfile(startdate,enddate, df,filename,bheader,"w")
 
