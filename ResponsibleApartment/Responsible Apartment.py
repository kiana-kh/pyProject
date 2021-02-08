def selectFromDict(options, name):
    index=0
    indexValidList = []
    print('Select the ' + name + ':')
    for optionName in options:
        index = index + 1
        indexValidList.extend([options[optionName]])
        print(str(index) + ') ' + optionName)
    inputValid = False
    while not inputValid:
            inputRaw = input(name + ': ')
            inputNo = int(inputRaw) - 1
            if inputNo > -1 and inputNo < len(indexValidList):
                selected = indexValidList[inputNo]
                print('Selected ' +  name + ': ' + selected)
                inputValid = True
                break
            else:
                print('Please select a valid ' + name + ' number')

    return selected


import csv

with open('data.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('data_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        Apartments = {rows[0]:rows[1] for rows in reader}
Apartments.pop('name',None)
Apartments['Default'] = 'Manager'
ResponsibleApartment = selectFromDict(Apartments, 'Responsible Apartment')
