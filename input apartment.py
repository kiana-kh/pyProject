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



options = {}

options['Default: Manager'] = 'Default: Manager'
options['Apartment 1'] = 'Apartment 1'
options['Apartment 2'] = 'Apartment 2'
options['Apartment 3'] = 'Apartment 3'
options['Apartment 4'] = 'Apartment 4'
options['Apartment 5'] = 'Apartment 5'
options['Apartment 6'] = 'Apartment 6'
options['Apartment 7'] = 'Apartment 7'
options['Apartment 8'] = 'Apartment 8'
options['Apartment 9'] = 'Apartment 9'
options['Apartment 10'] = 'Apartment 10'



option = selectFromDict(options, 'Responsible Apartment')
