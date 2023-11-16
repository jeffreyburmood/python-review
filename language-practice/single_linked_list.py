""" this script implements a singly linked list """

# just use a regular python list

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            node = self.head
            for i in range(self.size):
                if i == index:
                    return node.value
                else:
                    node = node.next

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            loc = self.head
            while loc.next != None:
                loc = loc.next
            loc.next = node
        self.size += 1



    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        else:
            node = self.head
            for i in range(self.size):
                if i == index:
                    remove_node = node.next
                    node.next = remove_node.next
                    self.size -= 1
                    return True
                else:
                    node = node.next


    def getValues(self) -> list[int]:
        value_list = []
        if self.size != 0:
            node = self.head
            for i in range(self.size):
                value_list.append(node.value)
                node = node.next

        return value_list


