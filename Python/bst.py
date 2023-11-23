class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.start = None
        self.amount = 0

    def insert(self, value):
        node = Node(value)
        if self.start == None:
            self.start = node
        else:
            tempNode = self.start
            while True:
                if tempNode.value > node.value:
                    if tempNode.left == None:
                        tempNode.left = node
                        break
                    tempNode = tempNode.left
                elif tempNode.value < node.value:
                    if tempNode.right == None:
                        tempNode.right = node
                        break
                    tempNode = tempNode.right

    def fromArray(self, array):
        for i in array:
            self.insert(i)

    def search(self, value):
        self.amount = 0
        if self.start == None:
            return False
        else:
            tempNode = self.start
            while True:
                self.amount += 1
                if tempNode.value == value:
                    return True
                elif tempNode.value > value:
                    if tempNode.value > value and tempNode.left == None:
                        return False
                    tempNode = tempNode.left
                elif tempNode.value < value:
                    if tempNode.value < value and tempNode.right == None:
                        return False
                    tempNode = tempNode.right


    def min(self):
        self.amount = 0
        if self.start == None:
            return False
        else:
            tempNode = self.start
            self.amount += 1
            while tempNode.left != None:
                self.amount += 1
                tempNode = tempNode.left
            return tempNode.value

    def max(self):
        self.amount = 0
        if self.start == None:
            return False
        else:
            tempNode = self.start
            self.amount += 1
            while tempNode.right != None:
                tempNode = tempNode.right
                self.amount += 1
            return tempNode.value

    def visitedNodes(self):
        return self.amount



