'''
Write a program to display all prime numbers within a range.

Author:Noor
Date:02/12/23
'''
start=int(input('Enter start range:'))
end=int(input('Enter end range:'))

for i in range(start,end+1):
    if(i>1):
        for p in range(2,i):
            if(i%p==0):
                break
        else:
            print('Prime numbers in range',start,',',end,'=',i)



            
    
    
    

