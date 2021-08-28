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
            if self.hasCycle():
                print("LinkedList contains a cycle, traversal will be infinite LOL!")
            else:
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

    def insertAfterValue(self, value, valueToBeInserted) -> bool:
        if self.isEmptyList():
            print("Empty list")
            return False

        else:
            node = self.headOfList
            while node is not None:
                if node.val == value:
                    newNode = LinkedListNodes.SinglyLinkedNode(val=valueToBeInserted)
                    newNode.setNext(node.getNext())
                    node.setNext(newNode)
                    self.length += 1
                    return True
                node = node.getNext()
        return False

    def insertValueInBeginning(self, value):
        newNode = LinkedListNodes.SinglyLinkedNode(value)
        if self.isEmptyList():
            self.headOfList = newNode
        else:
            newNode.setNext(self.headOfList)
            self.headOfList = newNode
        self.length += 1

    def __getitem__(self, item):
        if type(item) is not int:
            print("Please enter subscriptable index integers only")
            return None

        if self.isEmptyList():
            print("Empty list")
            return None

        if self.length < item:
            print("Index too large, list too small")
            return None
        counter = 0
        node = self.headOfList
        while counter != item:
            node = node.getNext()
            counter += 1
        return node.val

    def hasCycle(self) -> bool:
        if self.isEmptyList():
            return False
        slow = self.headOfList
        fast = self.headOfList.getNext()
        while slow.val != fast.val:
            if fast is None or fast.getNext() is None:
                return False
            slow = slow.getNext()
            fast = fast.getNext().getNext()
        return True
