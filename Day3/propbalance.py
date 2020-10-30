list1= [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

dict1= {x[0]:x[1] for x in list1 if x[1]>=x[2] }
print (dict1)

#dict of those with proper balances (above or equal min bal) {"Guido": 2000, "Brandon": 2000}