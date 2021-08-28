from LinkedList import LinkedListNodes


class SinglyLinkedList:

    def __init__(self, sourceList: list):
        lastInitializedNode: LinkedListNodes.SinglyLinkedNode or None = None
        self.headOfList: LinkedListNodes.SinglyLinkedNode or None = None
        self.length = len(list)
        for value in sourceList:
            node = LinkedListNodes.SinglyLinkedNode(val=value)
            if self.headOfList is None:
                self.headOfList = node
                lastInitializedNode = node
            if lastInitializedNode is not None:
                lastInitializedNode.setNext(node)
                lastInitializedNode = node

    def __len__(self):
        return self.length

    def traverseList(self):
        node = self.headOfList
        while node.getNext() is not None:
            print(node.val)
            node = node.getNext()
        print(node.val)
