# from LinkedList import DoublyLinkedList
from LinkedList import SinglyLinkedList

if __name__ == '__main__':
    singlyLinkedList = SinglyLinkedList.SinglyLinkedList([0, 1, 2, 3])
    singlyLinkedList.traverseList()
    singlyLinkedList.deleteValue(2)
    singlyLinkedList.traverseList()

    singlyLinkedList.deleteValue(3)
    singlyLinkedList.traverseList()

    singlyLinkedList.deleteValue(1)
    singlyLinkedList.traverseList()
    singlyLinkedList.traverseList()
    print(singlyLinkedList.deleteValue(0))
    singlyLinkedList.traverseList()
    # print(singlyLinkedList.findValue(4).val)
    # doublyLinkedList = DoublyLinkedList.DoublyLinkedList([0, 1, 2, 3])
    # doublyLinkedList.traverseListFromTail()
