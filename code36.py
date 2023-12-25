'''
write a function to check a prime number

Author:Noor
Date:23/12/23
'''

def  is_prime(num):
    if(num==0 or num==1):
        return(False)
    is_prime=True
    for i in range(2,num):
        if(num%i==0):
            is_prime=False
            break
    return(is_prime)

number=int(input('Enter a number:'))
check_prime=is_prime(number)
if(check_prime):
    print(number,'is prime.')
else:
    print(number,'is not prime.')
 
