'''
Problem 5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder. What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?

'''

def solve():
    n = 1
    minVal = 1
    maxVal = 20
    for i in range(minVal, maxVal+1):
        n = lcm(n, i)
    print(n)

def gcd(a,b):
    if(b):
        return (gcd(b,a%b))
    else:
        return a

def lcm(a,b):
    return a * b / gcd(a,b)

if __name__ == "__main__":
    solve()
