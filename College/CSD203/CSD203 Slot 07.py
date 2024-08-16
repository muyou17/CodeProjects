class Node(object):
    def __init__(self, data: int, next) -> None:
        self.data: int = data
        self.next: Node = next

    def display(self) -> None:
        print(self.data)


class SingleLinkedList(object):
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def isEmpty(self) -> bool:
        return self.head is None

    def addHead(self, new_data) -> None:
        new_node: Node = Node(new_data, None)
        if self.isEmpty():
            self.head: Node = new_node
            self.tail: Node = new_node
        else:
            new_node.next = self.head
            self.head: Node = new_node

    def addTail(self, new_data) -> None:
        new_node: Node = Node(new_data, None)
        if self.isEmpty():
            self.tail: Node = new_node
            self.head: Node = new_node
        else:
            self.tail.next = new_node
            self.tail: Node = new_node

    def removeHead(self) -> None:
        if self.isEmpty():
            return None
        self.head: Node = self.head.next

    def removeTail(self) -> None:
        if self.isEmpty():
            return None
        current: Node = self.head
        while current.next.next:
            current: Node = current.next
        self.tail: Node = current
        current.next = None

    def traversalDisplay(self) -> None:
        if self.isEmpty():
            print("The list is empty.")
        else:
            current: Node = self.head
            while current:
                current.display()
                current = current.next


def main() -> None:
    SSL: SingleLinkedList = SingleLinkedList()

    SSL.traversalDisplay()


if __name__ == '__main__':
    main()