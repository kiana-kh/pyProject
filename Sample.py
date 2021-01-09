import pandas as pd
with open("accounts.csv") as data:
    Accounts = pd.read_csv(data)
    print(Accounts) 
    Accounts.to_csv("newfile.csv",index=False)