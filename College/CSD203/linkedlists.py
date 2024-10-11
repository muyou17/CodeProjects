from functools import total_ordering
from collections.abc import Iterable, Iterator
from typing import Any


@total_ordering
class _Node(object):
    def __init__(self, data: Any) -> None:
        self.data = data

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, other) -> bool:
        if isinstance(other, _Node):
            return self.data == other.data
        return self.data == other

    def __lt__(self, other) -> bool:
        if isinstance(other, _Node):
            return self.data < other.data
        return self.data < other


class SLLNode(_Node):
    def __init__(self, data: Any) -> None:
        super().__init__(data)
        self.next = None


class DLLNode(_Node):
    def __init__(self, data: Any) -> None:
        super().__init__(data)
        self.next = self.previous = None


class _LinkedList(object):
    def __init__(self, *data: Any) -> None:
        self.head = self.tail = None
        self._length = 0
        for data in data:
            self.add_tail(data)

    def __repr__(self):
        return NotImplemented

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterator[_Node]:
        cursor = self.head
        while cursor is not None:
            yield cursor
            cursor = cursor.next

    def __getitem__(self, index: int) -> _Node:
        if index < 0:
            index += self._length
        if not self._length >= index >= 0:
            raise IndexError("Index out of range")

        cursor = self.head
        for _ in range(index):
            cursor = cursor.next
        return cursor

    def __setitem__(self, index: int, data: Any) -> None:
        cursor = self[index]
        cursor.data = data

    def __delitem__(self, index: int) -> None:
        self.remove_at(index)

    def __add__(self, other: Any):
        if isinstance(other, Iterable):
            for element in other:
                self.add_tail(element)
        elif isinstance(other, _Node):
            self.add_head(other.data)
        else: self.add_head(other)
        return self

    def __sub__(self, other: Any):
        if isinstance(other, Iterable):
            self.remove(*other)
        elif isinstance(other, _Node):
            self.remove(other.data)
        else: self.remove(other)
        return self

    def add_head(self, *data: Any):
        return NotImplemented

    def add_tail(self, *data: Any):
        return NotImplemented

    def add_at(self, index: int, data: Any):
        return NotImplemented

    def remove_head(self, amount: int):
        return NotImplemented

    def remove_tail(self, amount: int):
        return NotImplemented

    def remove_at(self, index: int):
        return NotImplemented

    def remove(self, *data: Any):
        if any(data not in self for data in data):
            return print("The list does not have these nodes.")

        for data in data:
            for index in range(self._length):
                if self[index].data == data:
                    return self.remove_at(index)

    def clear(self) -> None:
        self.head = self.tail = None
        self._length = 0

    def find(self, data: Any) -> int | None:
        for index, node in enumerate(self):
            if node == data:
                return index
        print("The list does not have this node")

    def sort(self, key=None, /, reverse: bool = False) -> None:
        cursor = self.head
        for data in sorted(self, key=key, reverse=reverse):
            cursor.data = data
            cursor = cursor.next

    def traverse(self, amount: int = 0) -> None:
        if self._length == 0:
            return print("The list is empty.")
        elif len(self) < amount:
            return print("The list does not have enough nodes for traversing.")

        elif amount <= 0:
            amount = self._length
        cursor = self.head
        for _ in range(amount):
            print(cursor)
            cursor = cursor.next


class SinglyLinkedList(_LinkedList):
    def __repr__(self) -> str:
        return f'SinglyLinkedList({', '.join(repr(node) for node in self)})'

    def add_head(self, *data: Any) -> None:
        for data in data:
            node = SLLNode(data)
            if self._length == 0:
                self.head = node
                self.tail = self.head
            else:
                node.next = self.head
                self.head = node
            self._length += 1

    def add_tail(self, *data: Any) -> None:
        for data in data:
            node = SLLNode(data)
            if self._length == 0:
                self.tail = node
                self.head = self.tail
            else:
                self.tail.next = node
                self.tail = node
            self._length += 1

    def add_at(self, index: int, data: Any) -> None:
        if index < 0:
            index += self._length
        if not self._length >= index >= 0:
            raise IndexError("Index out of range")

        if index == 0:
            self.add_head(data)
        elif index == self._length:
            self.add_tail(data)
        else:
            node = SLLNode(data)
            node.next = self[index]
            self[index - 1] = node

    def remove_head(self, amount: int = 1) -> None:
        if self._length < amount:
            return print("The list does not have enough nodes for deletion.")

        for node in range(amount):
            self.head = self.head.next
            self._length -= 1

    def remove_tail(self, amount: int = 1) -> None:
        if self._length < amount:
            return print("The list does not have enough nodes for deletion.")

        for node in range(amount):
            self.tail = self[-2]
            self.tail.next = None
            self._length -= 1

    def remove_at(self, index: int) -> None:
        if index < 0:
            index += self._length
        if not self._length > index >= 0:
            raise IndexError("Index out of range")

        if index == 0:
            return self.remove_head()
        elif index == self._length - 1:
            return self.remove_tail()
        cursor = self[index - 1]
        cursor.next = cursor.next.next
        self._length -= 1


class DoublyLinkedList(_LinkedList):
    def __repr__(self) -> str:
        return f'DoublyLinkedList({', '.join(repr(node) for node in self)})'

    def add_head(self, *data: Any) -> None:
        for data in data:
            node = DLLNode(data)
            if self._length == 0:
                self.head = node
                self.tail = self.head
            else:
                node.next = self.head
                self.head.previous = node
                self.head = node
            self._length += 1

    def add_tail(self, *data: Any) -> None:
        for data in data:
            node = DLLNode(data)
            if self._length == 0:
                self.tail = node
                self.head = self.tail
            else:
                node.previous = self.tail
                self.tail.next = node
                self.tail = node
            self._length += 1

    def add_at(self, index: int, data: Any) -> None:
        if index < 0:
            index += self._length
        if not self._length >= index >= 0:
            raise IndexError("Index out of range")

        if index == 0:
            self.add_head(data)
        elif index == self._length:
            self.add_tail(data)
        else:
            node = DLLNode(data)
            node.previous = self[index].previous
            node.next = self[index]
            self[index].previous.next = node
            self[index].previous = node
            self._length += 1

    def remove_head(self, amount: int = 1) -> None:
        if self._length < amount:
            return print("The list does not have enough nodes for deletion.")

        for node in range(amount):
            self.head = self.head.next
            self._length -= 1
            if self._length > 0:
                self.head.previous = None

    def remove_tail(self, amount: int = 1) -> None:
        if self._length < amount:
            return print("The list does not have enough nodes for deletion.")

        for node in range(amount):
            self.tail = self.tail.previous
            self._length -= 1
            if self._length > 0:
                self.tail.next = None

    def remove_at(self, index: int) -> None:
        if index < 0:
            index += self._length
        if not self._length >= index >= 0:
            raise IndexError("Index out of range")

        if index == 0:
            return self.remove_head()
        elif index == self._length - 1:
            return self.remove_tail()
        cursor = self[index].previous
        cursor.next = cursor.next.next
        cursor.next.previous = cursor
        self._length -= 1