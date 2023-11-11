'''
Write a program to find maximum between two numbers. Numbers should be user input.

Author:Noor
Date:11/11/23
'''

num1=int(input('enter a number:'))
num2=int(input('enter another number:'))
if (num1>num2):
    print(num1,'is maximum')
elif(num1==num2):
    print('Both numbers are equal')
    
else:
    print(num2,'is maximum')
    
