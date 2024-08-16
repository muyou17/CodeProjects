class Node(object):
    def __init__(self, data, prev, next) -> None:
        self.data = data
        self.prev: Node = prev
        self.next: Node = next

    def displayNode(self) -> None:
        print(self.data)


class DoublyLinkedList(object):
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def isEmpty(self) -> bool:
        return self.head is None

    def addHead(self, new_data) -> None:
        new_item: Node = Node(new_data, None, None)
        if self.isEmpty():
            self.head: Node = new_item
            self.tail: Node = new_item
        else:
            new_item.next = self.head
            self.head.prev = new_item
            self.head: Node = new_item

    def addTail(self, new_data) -> None:
        new_item: Node = Node(new_data, None, None)
        if self.isEmpty():
            self.tail: Node = new_item
            self.head: Node = new_item
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail: Node = new_item

    def removeHead(self) -> None:
        if self.isEmpty():
            return None
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def removeTail(self) -> None:
        if self.isEmpty():
            return None
        self.tail: Node = self.tail.prev
        if self.tail:
            self.tail.next = None

    def traversalDisplay(self) -> None:
        if self.isEmpty():
            print("The list is empty.")
        else:
            current = self.head
            while current:
                current.displayNode()
                current: Node = current.next


def main():
    DLL: DoublyLinkedList = DoublyLinkedList()

    DLL.addHead(5)
    DLL.addHead(4)
    DLL.removeHead()
    DLL.removeHead()

    DLL.traversalDisplay()


if __name__ == '__main__':
    main()