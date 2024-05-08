""" this script contains various methods for working with binary trees """

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildBinaryTree(values: list) -> TreeNode:
    binaryTree = []
    # set root node
    node = TreeNode(values[0])
    binaryTree.append(node)
    for i in range(1, len(values)):
        node = TreeNode(values[i])
        

# The eval() method parses the expression passed to this method and runs python expression (code) within the program.
def isBinaryTree(nodeList: list) -> str:
    # deal with the weird string-based tuples crap
    parentList = []
    for node in nodeList:
        child, parent = eval(node)
        parentList.append(parent)
        if parentList.count(parent) > 2:
            return 'false'
    return 'true'

def inorderTraversal(self, root: TreeNode) -> None:
    if root.left != None:
        self.inorderTraversal(root.left)
    self.ordered.append(root.val)
    if root.right != None:
        self.inorderTraversal(root.right)

def inorderTraversal(self, root: TreeNode) -> None:
    if root == None:
        return
    self.inorderTraversal(root.left)
    self.ordered.append(root.val)
    self.inorderTraversal(root.right)

@property
def ordered(self):
    return self.orderedResult


list1 = ['(1,2)', '(2,4)', '(5,7)', '(7,2)', '(9, 5)']
list2 = ['(1,2)', '(3,2)', '(2,12)', '(5,2)']

print(isBinaryTree(list1))
print(isBinaryTree(list2))