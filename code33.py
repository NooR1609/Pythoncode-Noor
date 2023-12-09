'''
Write a program to create function calculation such that it can accept two variables and calculate 
addition and subtraction. Also, it must return both addition and subtraction in a single return 
call.

Author:Noor
Date:09/12/23
'''

num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))

def addition_and_subtraction(X,Y):
    return(X+Y,X-Y)

addition,subtraction= addition_and_subtraction(num1,num2)
print(num1,'+',num2,'=',addition,'\n',num1,'-',num2,'=',subtraction,sep='')
