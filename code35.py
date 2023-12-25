'''
Write a program to create a function show_employee using the following conditions. 
o It should accept the employee’s name and salary and display both. 
o If the salary is missing in the function call then assign default value 9000 to salary.

Author:Noor
Date:09/12/23
'''
name=input("Enter The Name:")
salary=int(input('Enter The salary:'))

def show_employee(x,y=9000):
    print('Name:',x,'\n','Salary:',y,sep='')
    
show_employee(name,salary)
show_employee('Noor')







