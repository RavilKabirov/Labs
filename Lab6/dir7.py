with open('A.txt','r') as firstfile, open('B.txt','a') as secondfile:
    
    for line in firstfile:
             
             secondfile.write(line)