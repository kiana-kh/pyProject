import pandas 
with open("accounts.csv") as data:
    Accounts = pandas.read_csv(data)
    print(Accounts) 