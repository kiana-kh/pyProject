
def get_status(a:int,b:int,c:int,d:int):
    if d<=a:
        return "Green"
    elif d>a and d<=b :
        return "Orange"
    elif d>b and d<=c :
        return "Red"
    elif d>c:
        return "Insane"

