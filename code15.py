'''
Print the following pattern using the for loop 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

Author:Noor
Date:02/12/2023
'''
#num=int(input('Enter the Number'))
for i in range(1,5+1):
    for p in range(1,i+1):
        print(p,end=' ')
    print()

