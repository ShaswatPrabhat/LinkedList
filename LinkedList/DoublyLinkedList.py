from LinkedList import LinkedListNodes


class DoublyLinkedList:

    def __init__(self, sourceList: list):
        self.headOfList: LinkedListNodes.DoublyLinkedNode or None = None
        self.tailOfList: LinkedListNodes.DoublyLinkedNode or None = None
        self.length = len(list)
        for value in sourceList:
            node = LinkedListNodes.DoublyLinkedNode(val=value)
            if self.headOfList is None:
                self.headOfList = node
            if self.tailOfList is None:
                self.tailOfList = node
            else:
                self.tailOfList.setNext(node)
                node.setPrev(self.tailOfList)
                self.tailOfList = node

    def __len__(self):
        return self.length

    def traverseListFromHead(self):
        node = self.headOfList
        while node.getNext() is not None:
            print(node.val)
            node = node.getNext()
        print(node.val)

    def traverseListFromTail(self):
        node = self.tailOfList
        while node.getPrev() is not None:
            print(node.val)
            node = node.getPrev()
        print(node.val)
