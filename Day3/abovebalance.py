list1= [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

dict1= [(x[0],x[1]) for x in list1 if x[1]>0 ]
print (dict1)

#list of tuples with name and current balance if the balance is above 0 [("Guide", 2000), ("Jack", 900), ("Brandon", 2000)]