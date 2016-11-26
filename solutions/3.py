'''
Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math

def solve():
    n = 600851475143
    answer = round(math.sqrt(n))+1

    for i in range(answer,0,-1):
        if(isPrime(i) and n%i==0):
            answer = i
            break

    print(answer)

def isPrime(number):
    current = 0
    if number<2:
        return False;

    for i in range(2,round(math.sqrt(number))+1):
        if(number%i==0):
            return False;
    return True

if __name__ == "__main__":
    solve()
