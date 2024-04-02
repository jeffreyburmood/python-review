""" this script will calculate the factorial of a positive integer """

# 0! = 1
# n! = n * (n-1) * (n-2) ... * 1

def factorial(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))
print(factorial(0))
print(factorial(8))