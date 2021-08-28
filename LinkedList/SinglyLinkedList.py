from LinkedList import LinkedListNodes


class SinglyLinkedList:

    def __init__(self, sourceList: list):
        lastInitializedNode: LinkedListNodes.SinglyLinkedNode or None = None
        self.headOfList: LinkedListNodes.SinglyLinkedNode or None = None
        self.length = len(sourceList)
        for value in sourceList:
            node = LinkedListNodes.SinglyLinkedNode(val=value)
            if self.headOfList is None:
                self.headOfList = node
                lastInitializedNode = node
            if lastInitializedNode is not None:
                lastInitializedNode.setNext(node)
                lastInitializedNode = node

    def __len__(self) -> int:
        return self.length

    def isEmptyList(self) -> bool:
        return self.headOfList is None

    def traverseList(self) -> None:
        print("Traversing linked list")
        if not self.isEmptyList():
            node = self.headOfList
            while node.getNext() is not None:
                print(node.val)
                node = node.getNext()
            print(node.val)
        else:
            print("EMPTY LIST!!")

    def findValue(self, value) -> LinkedListNodes.SinglyLinkedNode or None:
        if not self.isEmptyList():
            node = self.headOfList
            while node.val != value:
                node = node.getNext()
            if node is not None:
                return node
            return None
        else:
            print("Empty List")

    def deleteFirstNode(self) -> bool:
        if not self.isEmptyList():
            self.headOfList = self.headOfList.getNext()
            self.length -= 1
            return True
        else:
            print("Empty list")
            return False

    def deleteLastNode(self) -> bool:
        if self.isEmptyList():
            print("Empty list")
            return False
        elif self.length == 1:
            self.headOfList = None
            self.length -= 1
            return True
        else:
            node = self.headOfList
            # Get the value from previous node of the next node
            # Change penultimate node to None
            while node.getNext().getNext() is not None:
                node = node.getNext()
            node.setNext(None)
            self.length -= 1
            return True

    def deleteValue(self, value) -> bool:
        if self.isEmptyList():
            print("Empty list")
            return False

        elif self.length == 1:
            if self.headOfList.val == value:
                self.headOfList = None
                self.length -= 1
                return True
            else:
                return False

        else:
            node = self.headOfList
            while node.getNext() is not None and node.getNext().val is not value:
                node = node.getNext()
            if node.getNext() is None:
                return False
            node.setNext(node.getNext().getNext())
            self.length -= 1
            return True
