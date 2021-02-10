def StatusColours():
    print("""
          we have Generally three statues 
          reporting the quality of total situation 
          based on the quantity of Manager's debt from Units
          you can manually enter the intervlas
          for each situation below
          *Green: when the debt is in this interval, 
          it seems quite satisfying:)
    
          *Yellow: when the debt is in this interval, 
          Manager should start to rethink
          
          *Red: maybe it's time to reconsider 
          the Manager's ability to Manage
          """)
          
    #Green
    Green_interval =input("The Green Interval is between 0 and?:")
    print("The Green interval of debts is (0,{})".format(Green_interval))
    #Yellow
    Yellow_interval =input("The Yellow Interval is between {} and?:".format(Green_interval))
    print("The Yellow interval of debts is ({},{})".format(Green_interval, Yellow_interval))
    #Red
    Red_interval =input("The Red Interval is between {} and?:".format(Yellow_interval))
    print("The Red interval of debts is ({},{})".format(Yellow_interval, Red_interval))
    return (int(Green_interval), int(Yellow_interval), int(Red_interval))