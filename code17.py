'''
Count the total number of digits in a number 
Example: Given a number 75869, output should be 5.

Author:Noor
Date:02/12/23
'''
num=int(input('Enter Number:'))
count_digit=0
while(num>0):
    count_digit=count_digit+1
    num=num//10
print(count_digit)
