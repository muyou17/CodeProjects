from typing import Any


class Node(object):
    def __init__(self, data: Any, next=None, prev=None) -> None:
        self.data: Any = data
        self.next: Node | None = next
        self.prev: Node | None = prev

    def display(self) -> None:
        print(self.data)


class DoublyCircularLinkedList(object):
    def __init__(self) -> None:
        self.head: None = None
        self.tail: None = None

    def addHead(self, data: Any) -> None:
        node: Node = Node(data)
        if self.head is None:
            self.head: Node = node
            self.tail: Node = node


def main() -> None:
    pass

if __name__ == "__main__":
    main()