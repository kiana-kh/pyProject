categories = ["Bills","Cleaning","Elevator","Parking","Repairment","Charge"]
subcategories = {"Bills":["Water","Electricity","Gas","Tax"]}
           
def category_input(categories,subcategories):

    loop = True

    while(loop):
        try:
             
            print("please enter the category or its number for this transaction. supported categories are:")
            print("   ".join("{}. {}".format(i[0],i[1]) for i in enumerate( categories,1)),"   0. Back")
            input_category = input().title()
        
            #adds the input in choosencategory but checks it for being number,string and indicates out of range inputs
            if(input_category.isnumeric()):
                if input_category=="0":
                    choosencategory = input_category
                    
                else :
                    choosencategory = categories[int(input_category)-1]
           
            elif (input_category in categories):
                choosencategory = input_category
           
            else:
                raise ValueError 
            loop = False
        except(ValueError,IndexError):
            print("wrong input. please check for your spelling or wheter your number or name is within range.")
    
    return(choosencategory)



def subcategory_input(categories,subcategories,choosencategory):
    
    loop = True

    while(loop):
        try:
            #subcategory process. pretty similar to category one   
            if(choosencategory in subcategories):

                print("This category has subcategories as listed below. please enter the subcategory or its number:")
                print("   ".join("{}. {}".format(i[0],i[1]) for i in enumerate(subcategories[choosencategory],1)),"   0. Back")   
                input_subcategory = input().title()

                if(input_subcategory.isnumeric()):
                    if input_subcategory=="0":
                        choosensubcategory = input_subcategory
                    else :
                        choosensubcategory = subcategories[choosencategory][int(input_subcategory)-1]
                elif (input_subcategory in subcategories[choosencategory]):
                    choosensubcategory = input_subcategory
                else:
                    raise ValueError
            else:
                choosensubcategory=float('nan')
            loop = False
        
        except(ValueError,IndexError):
            print("wrong input. please check for your spelling or wheter your number or name is within range.")
    
    return(choosensubcategory)