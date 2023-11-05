""" this script will return a comma-separated string containing a list of numbers representing an intersection """

def findIntersection(strArr):

    s1 = set(strArr[0].split(','))
    s2 = set(strArr[1].split(','))
    intersect = list(s1.intersection(s2))
    if len(intersect) == 0:
        return False
    intersect.sort()
    int_intersect = []
    for item in intersect:
        int_intersect.append(int(item))
    
    print(s1)
    print(s2)
    print(intersect)
    print(int_intersect)

findIntersection(['1,3,4,7,13', '1,2,4,13,15'])