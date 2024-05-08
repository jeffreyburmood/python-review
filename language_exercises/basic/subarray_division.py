""" Given an array A, find out how many unique subdivisions there are of size m that sum up to d """

def subarray_division(A:list, m, d:int) -> int:
    k = m
    c = 0
    q = []
    o = []
    for i in range(len(A)):
        q = []
        for j in range(i, k + i):
            if j != len(A):
                q.append(A[j])
            else:
                break
        o.append(q) # build a list of tuples of size m
    for i in o:
        if sum(i) == d:  # for each tuple determine if it sums to d
            c = c + 1
    return c
