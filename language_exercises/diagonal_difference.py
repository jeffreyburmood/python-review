""" Given a square matrix, calculate the absolute difference between the sums of its diagonals."""

def diagonalDifference(arr:list) -> int:
    listSize = len(arr)
    lrSum = 0
    rlSum = 0

    for i in range(0, listSize):
        for j in range(0, listSize):
            if i == j:
                lrSum += arr[i][j]
    print(lrSum)

    for i in range(0, listSize):
        j = listSize - 1 - i
        rlSum += arr[i][j]

    print(rlSum)

    return (abs(lrSum - rlSum))

print(diagonalDifference([[1,2,3], [4,5,6], [9,8,9]]))
print(diagonalDifference([[10, 20, 30, 40], [50,60,70,80], [12,13,14,15], [23, 24, 25, 26]]))