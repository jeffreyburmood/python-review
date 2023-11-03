""" working with various Python data structures """

# Lists (Arrays)
arr = [1, 2, 3]
print(arr)

arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

# initialize array of variable size
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# careful -1 index is not out of bounds
arr = [1, 2, 3]
print(arr[-1]) # reads the last value in the array
print(arr[-2]) # reads the next to the last value

# slicing an array
arr = [1, 2, 3, 4]
print(arr[1:3]) # the last index is non-inclusive
print(arr[0:4])

#unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# iterating through a list (array)
# with index
nums = [1, 2, 3]
for i in range(len(nums)):
    print(nums[i])

# without index
for num in nums:
    print(num)

# with index and value
for i, n in enumerate(nums):
    print(i, n)

# reverse an array
nums.reverse()
print(nums)

# sorting an array
arr = [5, 2, 3, 1, 4]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

# list comprehension
arr = [i for i in range(5)]
print(arr)

arr = [i+1 for i in range(5)]
print(arr)

# build 2D array with 4 elements
arr = [[0]*4 for i in range(4)]
print(arr)

# strings are similar to arrays
s = 'abc'
print(s[0:2])

# strings are immutable so updating a string creates a new string
s += 'def'
print(s)

# valid numeric strings can be converted to integers
print(int('123') + int('123'))

# and numbers can be converted to strings
print(str(123) + str(123))

# get ASCII value of a character
print(ord('a'))
print(ord('b'))

# queues - double ended queues
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
queue.pop()
print(queue)

# hashset
myset = set()
myset.add(1)
myset.add(2)
print(myset)
print(len(myset))

print(1 in myset)
print(2 in myset)
print(3 in myset)

myset.remove(2)
print(2 in myset)

# initialize a set with a list or set comprehension
print(set([1,2,3]))

myset = {i for i in range(5)}
print(myset)

# dictionaries - hashmaps




