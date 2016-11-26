'''
Problem 3:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

'''
def solve():
    answer = 0
    temp = 0

    for i in range(999,99,-1):
        for j in range(999,99,-1):
            temp = i*j
            if(isPalindrome(temp) and temp > answer ):
                answer = temp
    print(answer)

def isPalindrome(num):
    reverse = 0
    placeholder = num

    while(placeholder !=0):
        reverse = placeholder%10 + reverse*10
        placeholder= placeholder//10

    return True if(num==reverse) else False

if __name__ == "__main__":
    solve()
