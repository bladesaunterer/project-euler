'''
Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
import math

def solve():
    answer = 1
    numInput = 1000


    for a in range(1,numInput+1):
        for b in range(1,numInput+1):
                prod = a**2 + b**2
                c = math.sqrt(prod)
                if(c%1==0 and a+b+c==numInput and a<b<c):
                    answer = a*b*c

    print(answer)
