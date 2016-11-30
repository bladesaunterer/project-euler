'''
Problem 6:
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.

'''

def solve():
    sumOfSquares = 0
    squareOfSum = 0
    minVal = 1
    maxVal = 100

    for i in range(minVal,maxVal+1):
        sumOfSquares += i**2
        squareOfSum += i

    squareOfSum = squareOfSum**2

    print (squareOfSum - sumOfSquares)
