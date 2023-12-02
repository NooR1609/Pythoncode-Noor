'''
Print the following pattern using the for loop 
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 

Author:Noor
Date:02/12/2023
'''

for i in range(5,0,-1):
    for k in range(i,0,-1):
        print(k,end=" ")
    print()



