from typing import Any


class Node(object):
    def __init__(self, data: Any, next) -> None:
        self.data: Any = data
        self.next: Node = next

    def displayNode(self) -> None:
        print(self.data)


class CircularLinkedList(object):
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def isEmpty(self) -> bool:
        return self.head is None

    def addHead(self, new_data: Any) -> None:
        new_item: Node = Node(new_data, None)
        if self.isEmpty():
            self.head: Node | None = new_item
            self.tail: Node | None = new_item
        else:
            new_item.next = self.head
            self.tail.next = new_item
            self.head: Node | None = new_item

    def removeHead(self) -> None:
        if self.isEmpty():
            return None
        elif self.head == self.head.next:
            self.head: Node | None = None
        else:
            self.tail.next = self.head.next
            self.head: Node | None = self.head.next

    def addTail(self, new_data: Any) -> None:
        new_item: Node = Node(new_data, None)
        if self.isEmpty():
            self.head: Node | None = new_item
            self.tail: Node | None = new_item
        else:
            new_item.next = self.head
            self.tail.next = new_item
            self.tail: Node | None = new_item

    def removeTail(self) -> None:
        if self.isEmpty():
            return None
        if self.tail == self.tail.next:
            self.head: Node | None = None
            return None
        current: Node = self.head
        while current.next != self.tail:
            current: Node = current.next
        current.next = self.head

    def traversalDisplay(self) -> None:
        if self.isEmpty():
            print("The list is empty.")
        else:
            current: Node = self.head
            while True:
                current.displayNode()
                current = current.next
                if current == self.head:
                    return None
                

def main() -> None:
    CLL: CircularLinkedList = CircularLinkedList()

    CLL.addHead(4)
    CLL.addHead('abc')
    CLL.addTail('xyz')
    CLL.removeHead()
    CLL.removeHead()
    CLL.removeHead()
    CLL.addTail(999)
    CLL.addTail(987)
    CLL.addTail('dcm')
    CLL.removeHead()
    CLL.addHead(45)
    CLL.removeTail()

    CLL.traversalDisplay()


if __name__ == '__main__':
    main()