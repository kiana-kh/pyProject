d={1:['id1',2,1,125,1],2:['id2',1,1,75,1],
   3:['id3',4,2,125,1],4:['id4',4,2,75,1],
   5:['id5',7,3,125,2],6:['id6',3,3,75,1],
   7:['id7',2,4,125,1],8:['id8',6,4,75,1],
   9:['id9',5,5,125,2],10:['id10',5,5,75,1]}


x = [int(x) for x in input("""
     Enter the Percentage for each Apartment: 
     **Notes**
     Values should be seprated by space,
     the first number you put goes to the first apartment and so on,
     press Enter after you are done """).split()]
if len(x)!=len(d):
    print("Error! the number of your values must be {}".format(len(d)))
elif sum(x)!=100:
    print("Error! the Sum must be 100")
else:
    print(x)
    print("Are you sure, or do you want to retry? (Yes or No)"
    input = ""
    if input = "Yes":
        x = [int(x) for x in input("""
             Enter the Percentage for each Apartment: 
             **Notes**
             Values should be seprated by space,
             the first number you put goes to the first apartment and so on,
             press Enter after you are done """).split()]
        if len(x)!=len(d):
            print("Error! the number of your values must be {}".format(len(d)))
        elif sum(x)!=100:
            print("Error! the Sum must be 100")
        else:
            print(x)
    elif input = "NO":
        print("the Final List of percentages is:",x)
        
