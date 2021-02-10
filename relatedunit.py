

def append_relatedunit(data,allunits):
    
    if allunits==0:
        return(list(data.keys()))
    elif allunits==1:
        relatedunit=input('enter related units:\n').split(',')
        for e in relatedunit:
            if e not in list(data.keys()):
                print('wrong,try again')
                return(append_relatedunit(data,0))
        return relatedunit
    else:
        print('wrong,try again')
        return "repeat"

