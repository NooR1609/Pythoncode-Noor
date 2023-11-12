'''
Write a program to check whether a triangle is valid or not, Given all the three angles of the triangle as
user input.

Author:Noor
Date:12/11/23
'''

a1=int(input('Enter 1st angle:'))
a2=int(input('Enter 2nd angle:'))
a3=int(input('Enter 3rd angle:'))
if(a1>0 and a2>0 and a3>0):
    if (a1+a2+a3==180):
         print('Triangle is valid.')
        
else:
    print('Triangle is not valid.')
