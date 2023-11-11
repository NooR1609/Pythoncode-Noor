'''
Write a program to find maximum between three numbers. Numbers should be user input.

Author:Noor
Date:11/11/23
'''

num1=int(input('enter 1st number:'))
num2=int(input('enter 2nd number:'))
num3=int(input('enter 3rd number:'))

print('Maximum number is:',end='')
if (num1>num2)and (num1>num3):
    print(num1)
elif(num2>num1)and (num2>num3):
    print(num2)
else:
    print(num3)
    
