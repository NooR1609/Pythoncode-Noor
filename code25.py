'''
Write a program to print multiplication table of a given number.

Author:Noor
Date:09/12/23
'''
num=int(input('Enter Number: '))
for i in range(11):
    print(num,'*',i,'=',num*i,sep='')
