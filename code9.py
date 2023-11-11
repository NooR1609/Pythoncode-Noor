'''
Write a code that prints true only if given two user input numbers has same sign (either + or -)

Author:Noor
Date:11/11/23
'''

num1=int(input('enter a number:'))
num2=int(input('enter another number:'))
if(num1>0 and num2>0):
    print('True.')
elif(num1<0 and num2<0):
    print('True.')
else:
    print('False.')
    
    
    
