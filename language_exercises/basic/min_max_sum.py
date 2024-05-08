"""Given five positive integers, find the minimum and maximum values
that can be calculated by summing exactly four of the five integers. """

def minMaxSum(numberList:list) -> None:
    # first sort the array to ensure decending order
    numberList.sort()
    minSum = 0
    maxSum = 0
    for i in range(0, len(numberList)-1):
        minSum += numberList[i]
    for i in range(1, len(numberList)):
        maxSum += numberList[i]

    print(minSum, maxSum)

minMaxSum([1,3,5,7,9])
