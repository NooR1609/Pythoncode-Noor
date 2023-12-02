'''
Write a program to print the following star pattern using the for loop 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

Author:Noor
Date:02/12/23
'''


for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

for i in range(5,0,-1):
    for k in range(1,i+1):
        print('*',end=' ')
    print()




    
    
