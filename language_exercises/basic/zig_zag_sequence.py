""" Given an array of  distinct integers, transform the array into a zig zag sequence by permuting the array elements.
A sequence will be called a zig zag sequence if the first elements in the sequence are in increasing order and the
last  elements are in decreasing order, where k = (n+1)/2 """

def findZigZagSequence(a: list, n: int) -> None:
    a.sort()
    mid = int((n + 1)/2)-1 # adjust for list index
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = st + 1
    while(a[st] <= a[ed]):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

print(findZigZagSequence([2,3,5,1,4], 5))
print(findZigZagSequence([1,2,3,4,5,6,7], 7))