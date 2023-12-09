'''
Find the factorial of a given number

Author:Noor
Date:09/12/23
'''

num=int(input('Enter a number: '))

factorial=1

for i in range(1,num+1):
    factorial=factorial*i

print('Factorial of',num,'=',factorial)
