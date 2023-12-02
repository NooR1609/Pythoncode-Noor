'''
Sum the digits in a number. 
Example: Given a number 75869, output should be 35.

Author:Noor
Date:02/12/23
'''
num=int(input('Enter Number:'))
sum_digit=0
while(num>0):
    sum_digit=sum_digit+num%10
    num=num//10
print(sum_digit)
