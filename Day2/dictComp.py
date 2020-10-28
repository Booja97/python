def Convert(list1):
    square = {list1[i]: list1[i]*list1[i] for i in range(0, len(list1))}
    print(square.values())
    print(square)
        
list1 = [ 1, 2, 3]
Convert(list1)