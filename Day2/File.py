  
text = """File content
          This content comes from file"""
  
file1 = open('myfile.txt', 'w') 
file1.writelines(text) 
file1.close() 
  
file1 = open('myfile.txt', 'r') 
  
while True: 
   
    line = file1.readline() 
  
    if not line: 
        break
    print("{}".format( line.strip()), end ="\n") 
  
file1.close() 