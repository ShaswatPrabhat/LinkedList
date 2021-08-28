class SinglyLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next: SinglyLinkedNode or None = None

    def setNext(self, node: 'SinglyLinkedNode'):
        self.next = node

    def getNext(self):
        return self.next


class DoublyLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next: DoublyLinkedNode or None = None
        self.prev: DoublyLinkedNode or None = None

    def setPrev(self, node: 'DoublyLinkedNode'):
        self.prev = node

    def setNext(self, node: 'DoublyLinkedNode'):
        self.next = node

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev
