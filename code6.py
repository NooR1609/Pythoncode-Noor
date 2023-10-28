'''
write a program to check whether a number is divisible by 5 and 11 or not.

Author: Noor
Date:28/10/23
'''
num=int(input('write a number:'))
if (num%5==0 and num%11==0):
    print('number',num,'is divisible by 5 and 11')
else:
    print('number',num,'is not divisible by 5 and 11')
    
