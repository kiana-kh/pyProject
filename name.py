
def filterunits(data:dict,numberlist:list):
    newdata=data.copy()
    for e in list(data.keys()):
        if e not in numberlist:
            del newdata[e]
    name=[]
    for i in list(newdata.keys()):
        name.append(newdata[i][0])
    return newdata,name

