import csv

with open('data.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('data_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        Apartments = {rows[0]:rows[1] for rows in reader}
Apartments.pop('name',None)