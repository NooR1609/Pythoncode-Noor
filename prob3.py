'''
P-1:Write a function to print All the armstrong num from 1 to 1000
Armstrong number are special mnumber with property.
153=1**3+5**3+3**3=1+125+27=153
'''

num1=1
num2=1000

for num in range(num1,num2+ 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)
