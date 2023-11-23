class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None


    def add(self, node):
        if self.head == None:
            self.head = node
        elif node.data.price < self.head.data.price:
            node.nextNode = self.head
            self.head.prevNode = node
            self.head = node
        else:
            tempNode = self.head
            while tempNode.nextNode != None:
                if tempNode.nextNode.data.price > node.data.price:
                    break
                tempNode = tempNode.nextNode
            if tempNode.nextNode == None:
                tempNode.nextNode = node
                node.prevNode = tempNode
            else:
                node.nextNode = tempNode.nextNode
                node.prevNode = tempNode
                tempNode.nextNode.prevNode = node
                tempNode.nextNode = node

    def clean(self):
        self.head = None


class Car:
    def __init__(self, identification: int, name: str, brand: str, price: int, active: bool):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars):
    for i in cars:
        add(i)


def add(car):
    node = Node(None, None, car)
    db.add(node)


def updateName(identification, name):
    id = identification
    tempNode = db.head
    while tempNode.nextNode != None:
        if tempNode.data.identification == id:
            break
        tempNode = tempNode.nextNode
    if tempNode.nextNode == None and tempNode.data.identification != id:
        return
    else:
        tempNode.data.name = name


def updateBrand(identification, brand):
    id = identification
    tempNode = db.head
    while tempNode.nextNode != None:
        if tempNode.data.identification == id:
            break
        tempNode = tempNode.nextNode
    if tempNode.nextNode == None and tempNode.data.identification != id:
        return
    else:
        tempNode.data.brand = brand


def activateCar(identification):
    id = identification
    tempNode = db.head
    while tempNode.nextNode != None:
        if tempNode.data.identification == id:
            break
        tempNode = tempNode.nextNode
    if tempNode.nextNode == None and tempNode.data.identification != id:
        return
    else:
        tempNode.data.active = True


def deactivateCar(identification):
    id = identification
    tempNode = db.head
    while tempNode.nextNode != None:
        if tempNode.data.identification == id:
            break
        tempNode = tempNode.nextNode
    if tempNode.nextNode == None and tempNode.data.identification != id:
        return
    else:
        tempNode.data.active = False


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    price = 0
    tempNode = db.head

    while tempNode.nextNode != None:
        if tempNode.data.active == True:
            price += tempNode.data.price
        tempNode = tempNode.nextNode
    if tempNode.nextNode == None and tempNode.data.active == True:
        price += tempNode.data.price
    return price


def clean():
    db.clean()

