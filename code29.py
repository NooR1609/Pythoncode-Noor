'''
The sum of the squares of the first ten natural numbers is,
                                                 1**2+2**2+.....+10**2=385

The square of the sum of the first ten natural numbers is,
                                                 (1+2+....+10)**2=55**2=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025-385=2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
sum_=0
for i in range(1,101):
    
    sqr=i**2
    sum_= sum_+sqr
print('sum of the squares of the first one hundred natural numbers is:',sum_)

sum_n=0
sqr_n=0
for j in range(1,101):
    sum_n+=(j)
    sqr_n=sum_n**2
print('square of the sum of the first one hundred natural numbers is:',sqr_n)

diff_=(sqr_n-sum_)
print('diff b/w sum of the sqr of the 1st one hundred natural no. and the sqr of the sum:',sqr_n,'-',sum_,'=',diff_)
