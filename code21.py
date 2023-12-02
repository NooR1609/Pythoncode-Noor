'''
Write a program to display all prime numbers within a range.

Author:Noor
Date:02/12/23
'''
start=int(input('Enter start range:'))
end=int(input('Enter end range:'))

prime_counter=0

for i in range(start,end+1):
    num=i
    is_prime=True
    for p in range(2,num):
        if(num%p==0):
            is_prime=False
    if(is_prime and (num!=1)):
        prime_counter=prime_counter+1

print('Prime numbers in range',start,',',end,'=',prime_counter)
            
    
    
    

