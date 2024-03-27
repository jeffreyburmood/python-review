""" Another sorting method, the counting sort, does not require comparison.
Instead, you create an integer array whose index range covers the entire range of values in your array to sort.
Each time a value occurs in the original array, you increment the counter at that index. At the end,
run through your counting array, printing the value of each non-zero valued index that number of times."""

def countingSort(arr:list) -> list:
    result = [0 for i in range(0, 10)]

    for i in range(0, len(arr)):
        result[arr[i]-1] += 1

    return result

print(countingSort([2, 1, 3, 10, 10, 5, 5, 7, 1]))
print(countingSort([1, 1, 1, 2, 3, 6, 6, 10]))