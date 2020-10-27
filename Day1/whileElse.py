print("Enter the range of number to be printed:")
range= int(input())
number=1
while number <= range:
    print(number, end=' ')
    number+=1
else:
    print("\n")
    print("Number exceed the range")