"""Given an array of integers, where all elements but one occur twice, find the unique element."""

def lonelyInteger(arr:list) -> int:
    for element in arr:
        if(arr.count(element) < 2):
            return element

print(lonelyInteger([1,2,3,4,3,2,1]))
print(lonelyInteger([23,45,67,23,90,45,90]))