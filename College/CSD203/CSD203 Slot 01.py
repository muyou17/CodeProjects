from typing import Any


class KeyValue(object):
    def __init__(self, key: int, value: Any) -> None:
        self.key: int = key
        self.value: Any = value


class Node(object):
    def __init__(self, data: Any, next=None, prev=None) -> None:
        self.data: Any = data
        self.next: Node | None = next
        self.prev: Node | None = prev

    def display(self) -> None:
        print(self.data)


class SingleLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def addHead(self, new_data) -> None:
        new_node: Node = Node(new_data)
        if not self.head:
            self.head: Node = new_node
            self.tail: Node = new_node
        else:
            new_node.next = self.head
            self.head: Node = new_node

    def addTail(self, new_data) -> None:
        new_node: Node = Node(new_data)
        if not self.tail:
            self.tail: Node = new_node
            self.head: Node = new_node
        else:
            self.tail.next = new_node
            self.tail: Node = new_node

    def removeHead(self) -> None:
        if self.head:
            self.head: Node = self.head.next

    def removeTail(self) -> None:
        if self.tail:
            current: Node = self.head
            while current.next.next:
                current: Node = current.next
            self.tail: Node = current
            current.next = None

    def traversalDisplay(self) -> None:
        if not self.head:
            print("The list is empty.")
        else:
            current: Node = self.head
            while current:
                current.display()
                current = current.next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def addHead(self, new_data) -> None:
        new_item: Node = Node(new_data, None, None)
        if not self.head:
            self.head: Node = new_item
            self.tail: Node = new_item
        else:
            new_item.next = self.head
            self.head.prev = new_item
            self.head: Node = new_item

    def addTail(self, new_data) -> None:
        new_item: Node = Node(new_data, None, None)
        if not self.tail:
            self.tail: Node = new_item
            self.head: Node = new_item
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail: Node = new_item

    def removeHead(self) -> None:
        if not self.head:
            return None
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def removeTail(self) -> None:
        if not self.tail:
            return None
        self.tail: Node = self.tail.prev
        if self.tail:
            self.tail.next = None

    def traversalDisplay(self) -> None:
        if not self.head:
            print("The list is empty.")
        else:
            current = self.head
            while current:
                current.display()
                current: Node = current.next


class CircularLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def addHead(self, new_data: Any) -> None:
        new_item: Node = Node(new_data, None)
        if not self.head:
            self.head: Node | None = new_item
            self.tail: Node | None = new_item
        else:
            new_item.next = self.head
            self.tail.next = new_item
            self.head: Node | None = new_item

    def removeHead(self) -> None:
        if self.head:
            if self.head == self.head.next:
                self.head: Node | None = None
            else:
                self.tail.next = self.head.next
                self.head: Node | None = self.head.next

    def addTail(self, new_data: Any) -> None:
        new_item: Node = Node(new_data, None)
        if not self.tail:
            self.head: Node | None = new_item
            self.tail: Node | None = new_item
        else:
            new_item.next = self.head
            self.tail.next = new_item
            self.tail: Node | None = new_item

    def removeTail(self) -> None:
        if self.tail:
            if self.tail == self.tail.next:
                self.head: Node | None = None
                self.tail: Node | None = None
            else:
                current: Node = self.head
                while current.next != self.tail:
                    current: Node = current.next
                current.next = self.head

    def traversalDisplay(self) -> None:
        if not self.tail:
            print("The list is empty.")
        else:
            current: Node = self.head
            while True:
                current.display()
                current = current.next
                if current == self.head:
                    return None


class DoublyCircularLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def addHead(self, data: Any) -> None:
        node: Node = Node(data)
        if self.head is None:
            self.head: Node = node
            self.tail: Node = self.head
            self.head.next = self.tail
            self.tail.prev = self.head
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = self.head
            self.head: Node = node

    def addTail(self, data: Any) -> None:
        node: Node = Node(data)
        if self.tail is None:
            self.head: Node = node
            self.tail: Node = self.head
            self.head.next = self.tail
            self.tail.prev = self.head
            self.head.prev = self.tail
            self.tail.next = self.head

    def removeHead(self) -> None:
        if not self.head:
            return None


class Queue:
    def __init__(self) -> None:
        self.list: DoublyLinkedList = DoublyLinkedList()

    def enqueue(self, data: Any) -> None:
        self.list.addHead(data)

    def dequeue(self) -> Any:
        yield self.list.tail
        self.list.removeTail()

    def traversalDisplay(self) -> None:
        self.list.traversalDisplay()


class PriorityQueue:
    def __init__(self) -> None:
        self.list: DoublyLinkedList = DoublyLinkedList()

    def enqueue(self, key: int, value: Any) -> None:
        new_item: Node = Node(KeyValue(key, value))
        if not self.list.head:
            self.list.addHead(new_item)
        else:
            current: Node = self.list.head
            while current:
                if current.data > new_item.data.key:
                    new_item.next = current
                    new_item.prev = current.prev
                    if current.prev:
                        current.prev.next = new_item
                    else:
                        self.list.head = new_item
                    current.prev = current
                    break
            else:
                new_item.prev = self.list.tail
                self.list.tail.prev = new_item
                self.list.tail = new_item

    def dequeue(self) -> None:
        if self.list.head:
            self.list.head.display()
            self.list.head = self.list.head.next
            if self.list.head:
                self.list.head.prev = None

    def traversalDisplay(self) -> None:
        self.list.traversalDisplay()


class Heap(object):
    pass


class AdaptablePriorityQueue(PriorityQueue):
    pass