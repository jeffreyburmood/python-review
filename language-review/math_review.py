
# decimal division
print(5 / 2)

# integer division
print(5 // 2)
# negative number round down
print(-3 // 2) # rounds to -2 not -1

# get around this by doing decimal division and converting to integer
print(int(-3 / 2))

# modulo provides remainder
print(10 % 3)

# run into rounding issue again with negative numbers
print(-10 % 3)
# can be consistent with other languages by using math package
import math
print(math.fmod(-10, 3))

print(math.floor(3 / 2)) # round down
print(math.ceil(3 / 2)) # round up
print(math.sqrt(2))
print(math.pow(2, 3))

# max / min int
float("inf")
float('-inf')

print(math.pow(2, 200) < float("inf"))

