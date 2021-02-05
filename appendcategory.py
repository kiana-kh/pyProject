
def category_input():

    loop = True

    while(loop):
        try:
            categories = ["Bill","Cleaning","Elevator","Parking","Repairment","Charge"]
            subcategories = {"Bill":["Water","Electricity","gas"]}
            choosencategory=[]
            inputs=[]
            print("please enter the category or its number for this transaction. supported categories are:")
            print("   ".join("{}. {}".format(i[0],i[1]) for i in enumerate(categories,1)))
            inputs.append(input().title())
        
            #adds the input in choosencategory but checks it for being number,string and indicates out of range inputs
            if(inputs[0].isnumeric()):
                choosencategory.append(categories[int(inputs[0])-1])
            elif (inputs[0] in categories):
                choosencategory.append(inputs[0])
            else:
                raise ValueError 

            #subcategory process. pretty similar to category one   
            if(choosencategory[0] in subcategories):

                print("This category has subcategories as listed below. please enter the subcategory or its number:")
                print("   ".join("{}. {}".format(i[0],i[1]) for i in enumerate(subcategories[choosencategory[0]],1)))   
                inputs.append(input().title())

                if(inputs[1].isnumeric()):
                    choosencategory.append(subcategories[choosencategory[0]][int(inputs[1])-1])
                elif (inputs[1] in subcategories[choosencategory]):
                    choosencategory.append(inputs[1])
                else:
                    raise ValueError
            else:
                choosencategory[1]=float('nan')
            loop = False
        
        except(ValueError,IndexError):
            print("wrong input. please check for your spelling or wheter your number or name is within range.")
    
    return(choosencategory)