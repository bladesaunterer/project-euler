'''
Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10 001st prime number?

'''
import math

def solve():
    counter = 0
    answer = 0

    while (counter != 10001):
        answer +=1
        if(isPrime(answer)):
            counter +=1


    print(answer)



def isPrime(number):
    current = 0
    if number<2:
        return False;

    for i in range(2,round(math.sqrt(number))+1):
        if(number%i==0):
            return False;
    return True
