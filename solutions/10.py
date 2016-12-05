'''
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
import math

def solve():
    currentPrime = 2
    inputNum = 2000000
    answer = 0
    for i in range(inputNum+1):
        if(isPrime(i)):
            answer = answer+i

    print(answer)


def isPrime(number):
    if(number<2):
        return False

    for i in range(2,round(math.sqrt(number))+1):
        if(number%i==0):
            return False

    return True
