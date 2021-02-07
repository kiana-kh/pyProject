b=input('if all units are relatedunit type 0,else type 1')
def append_relatedunit():
    if b==0:
        print(d[['number']])
    elif b==1:
        relatedunit=input('enter relatedunit')
        relatedunitt=[]
        maax=d['number'].max()
        def related_unit():
            if relatedunit > maax:
                print('wrong,try again')
                return(related_unit)
            else:
                relatedunitt.append(relatedunit).split(',') 
          
