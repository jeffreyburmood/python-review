""" return the median element of an odd numbered list """


def findMedian(arr:list) -> int:

    arr.sort()
    medianIndex = round(len(arr) / 2)
    return(arr[medianIndex])

print(findMedian([3,1,4,2,5]))
print(findMedian([45,23,67,90,12]))
