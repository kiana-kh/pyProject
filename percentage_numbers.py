def percentage_input(d):
    x = [int(x) for x in input("""Enter the Percentage for each Apartment: 
         **Notes**
         Values should be integers separated by space,
         the first number you put goes to the first apartment and so on,
         press Enter after you are done \n""").split()]
    if len(x)!=len(d):
        print("Error! the number of your values must be {}".format(len(d)))
        return percentage_input(d)
    elif sum(x)!=100:
        print("Error! the Sum must be 100")
        return percentage_input(d)
    else:
        print("the List of percentages is:",x)
        print("Are you sure, or do you want to retry? (Yes or No)")
        retry = input()
        if retry.title() == "Yes":
            return percentage_input(d)
        elif retry.title() == "No":
            return x
        else:
            print("Error! PLease try again")
            return percentage_input(d)

