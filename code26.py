'''
Reverse a given integer number.

Author:Noor
Date:09/12/23
'''

num=int(input('Enter a number: '))

rev_digit = 0
while(num>0):
    rev_digit = rev_digit*10 + num%10
    num=num//10
print(rev_digit)
