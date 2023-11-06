""" this script contains various methods for working with binary trees """

def binaryTreeConstructor(nodeList: list) -> str:
    # deal with the weird string-based tuples crap
    parentList = []
    for node in nodeList:
        child, parent = eval(node)
        parentList.append(parent)
        if parentList.count(parent) > 2:
            return 'false'
    return 'true'


list1 = ['(1,2)', '(2,4)', '(5,7)', '(7,2)', '(9, 5)']
list2 = ['(1,2)', '(3,2)', '(2,12)', '(5,2)']

print(binaryTreeConstructor(list1))
print(binaryTreeConstructor(list2))