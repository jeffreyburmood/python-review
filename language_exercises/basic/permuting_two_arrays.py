""" There are two -element arrays of integers, A and B. Permute them into some A' and B' such that
    the relation A'[i] + B'[i] >= k holds for all i where 0<=i<n.
    There will be q queries consisting of A, B, and k. For each query, return YES if some permutation A", B',
    satisfying the relation exists. Otherwise, return NO."""

def two_arrays(k:int, A:list, B:list) -> str:
    A_prime = sorted(A)
    B_prime = sorted(B, reverse=True)

    for i in range(0, len(A)):
        if A_prime[i] + B_prime[i] < k:
            return 'NO'

    return 'YES'

print(two_arrays(1, [0,1], [0,2]))
print(two_arrays(10, [2,1,3], [7,8,9]))
print(two_arrays(5, [1,2,2,1], [3,3,3,4]))