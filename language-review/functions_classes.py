# functions

def myFunc(n, m):
    return n*m

print(myFunc(3,4))

# Nested functions - useful in recursion problems
def outer(a, b):
    c = 'c'

    def inner():
        return a + b + c

    return inner()

print(outer('a', 'b'))

# classes
class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    def getLength(self) -> int:
        return self.size

    def getDoubleLength(self) -> int:
        return 2 * self.getLength()

    