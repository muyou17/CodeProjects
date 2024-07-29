from typing import Any
import linkedlists


class Node(linkedlists.Node):
    def __init__(self, key: int, data: Any):
        self.key: int = key
        linkedlists.Node.__init__(self, data)


class PriorityQueue(object):
    def __init__(self):
        self.list = linkedlists.DoublyLinkedList()

    def add(self, key: int, data: Any) -> None:
        node: Node = Node(key, data)
        if self.list.isEmpty():
            self.list.addHead(node)
            self.list.addTail(node)
        else:
            current: Node = self.list.head
            while current.key < node.key:
                if current.next is None:
                    self.list.addTail(node)
                    return None
                current = current.next
            if current is self.list.head:
                self.list.addHead(node)
            else:
                before: Node = current.prev
                before.next = node
                node.prev = before
                current.prev = node
                node.next = current


class Heap(object):
    pass


class AdaptablePriorityQueue(PriorityQueue):
    pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()