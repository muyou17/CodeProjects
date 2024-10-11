from functools import total_ordering
from types import FunctionType, NotImplementedType
from collections.abc import Iterable, Iterator, Generator
from typing import Any


@total_ordering
class SLLNode(object):
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, other) -> bool:
        if isinstance(other, SLLNode):
            return self.data == other.data
        return self.data == other

    def __lt__(self, other) -> bool:
        if isinstance(other, SLLNode):
            return self.data < other.data
        return self.data < other


class DLLNode(SLLNode):
    def __init__(self, data: Any) -> None:
        super().__init__(data)
        self.previous = None


class _LinkedList(object):
    def __init__(self, *data: Any) -> None:
        self.head = self.tail = None
        self._length = 0
        if len(data) == 1 and isinstance(data[0], Iterable):
            for data in data[0]:
                self.add_tail(data)
        else:
            for data in data:
                self.add_tail(data)

    def __repr__(self) -> NotImplementedType:
        return NotImplemented

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterator[SLLNode]:
        cursor = self.head
        while cursor is not None:
            yield cursor
            cursor = cursor.next

    def __getitem__(self, index: int) -> SLLNode:
        if index < 0:
            index += self._length
        if not self._length > index >= 0:
            raise IndexError("Index out of range.")

        cursor = self.head
        for _ in range(index):
            cursor = cursor.next
        return cursor

    def __setitem__(self, index: int, data: Any) -> None:
        cursor = self[index]
        cursor.data = data

    def __delitem__(self, index: int) -> None:
        self.remove_at(index)

    def __add__(self, other: Any) -> 'LinkedList':
        if isinstance(other, Iterable):
            for element in other:
                self.add_tail(element)
        elif isinstance(other, SLLNode):
            self.add_head(other.data)
        else: self.add_head(other)
        return self

    def __sub__(self, other: Any) -> 'LinkedList':
        if isinstance(other, Iterable):
            self.remove(*other)
        elif isinstance(other, SLLNode):
            self.remove(other.data)
        else: self.remove(other)
        return self

    def add_head(self, *data: Any) -> NotImplementedType:
        """Add new nodes to the head of the list with the given data."""
        return NotImplemented

    def add_tail(self, *data: Any) -> NotImplementedType:
        """Add new nodes to the tail of the list with the given data."""
        return NotImplemented

    def add_at(self, index: int, data: Any) -> NotImplementedType:
        """Add a new node at the specified index with the given data."""
        return NotImplemented

    def remove_head(self, amount: int) -> NotImplementedType:
        """Remove nodes at the head of the list with the specified amount."""
        return NotImplemented

    def remove_tail(self, amount: int) -> NotImplementedType:
        """Remove nodes at the tail of the list with the specified amount."""
        return NotImplemented

    def remove_at(self, index: int) -> NotImplementedType:
        """Remove the node at the given index from the list."""
        return NotImplemented

    def remove(self, *data: Any) -> NotImplementedType | None:
        """Remove nodes with the given data from the list."""
        if any(data not in self for data in data):
            raise ValueError("The list does not have these nodes.")

        for data in data:
            for index in range(self._length):
                if self[index].data == data:
                    return self.remove_at(index)

    def clear(self) -> None:
        """Delete all nodes from the list."""
        self.head = self.tail = None
        self._length = 0

    def find(self, data: Any) -> int | None:
        """Find the index of the first node with the given data from the list."""
        for index, node in enumerate(self):
            if node == data:
                return index
        raise ValueError("The list does not have this node.")

    def find_all(self, data: Any) -> Generator[int, None, None] | None:
        """Find indexes of all nodes with the given data from the list."""
        found = False
        for index, node in enumerate(self):
            if node == data:
                yield index
                found = True
        if not found:
            raise ValueError("The list does not have this node.")

    def _insertion_sort(self, start: int, end: int, key: FunctionType, reverse: bool) -> SLLNode:
        """Insertion sort between indices start and end implemented as a helper method for Timsort."""
        for first_index in range(start + 1, end):
            cursor = self[first_index]
            second_index = first_index - 1
            while second_index >= start and (key(self[second_index].data) > key(cursor.data)) ^ reverse:
                self[second_index].next.data = self[second_index].data
                second_index -= 1
            self[second_index].next.data = cursor.data
        return self[start]

    def _merge(self, left: SLLNode, right: SLLNode, key: FunctionType, reverse: bool) -> SLLNode:
        """Helper method to merge two sorted list runs for Timsort."""
        tail = dummy = SLLNode(None)
        while left is not None and right is not None:
            if (key(left.data) < key(right.data)) ^ reverse:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next

    def _update_tail(self) -> None:
        """Helper method to update the tail pointer for Timsort."""
        cursor = self.head
        while cursor.next:
            cursor = cursor.next
        self.tail = cursor

    def sort(self, key: FunctionType = lambda x: x, reverse: bool = False) -> None:
        """Sort the list with the optional given key using the Timsort algorithm."""
        MAX_RUN = 32

        # Split the list into small runs and sort each run with insertion sort
        index = 0
        sorted_runs = SinglyLinkedList()
        while index < self._length:
            run_size = min(MAX_RUN, self._length - index)
            sorted_run = self._insertion_sort(index, index + run_size, key, reverse)
            sorted_runs.add_tail(sorted_run)
            index += run_size

        # Merge sorted runs
        while len(sorted_runs) > 1:
            new_runs = SinglyLinkedList()
            for index in range(0, len(sorted_runs), 2):
                if index + 1 < len(sorted_runs):
                    merged = self._merge(sorted_runs[index], sorted_runs[index + 1], key, reverse)
                    new_runs.add_tail(merged)
                else:
                    new_runs.add_tail(sorted_runs[index])
            sorted_runs = new_runs

        # Update the head and tail
        self.head = sorted_runs.head
        self._update_tail()

    def traverse(self, amount: int = 0, separator: str = ' ', end: str = '\n') -> None:
        """Traverse the list with the given amount of nodes."""
        if self._length == 0:
            return print("The list is empty.")
        elif self._length < amount:
            return print("The list does not have enough nodes for traversing.")
        elif amount <= 0:
            amount = self._length - 1
        else: amount -= 1

        for index, node in enumerate(self):
            if index == amount:
                return print(node, end=end)
            print(node, end=separator)


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
            raise IndexError("Index out of range.")

        if index == 0:
            self.add_head(data)
        elif index == self._length:
            self.add_tail(data)
        else:
            node = SLLNode(data)
            node.next = self[index]
            self[index - 1] = node

    def remove_head(self, amount: int = 1) -> None:
        if self._length <= amount:
            self.clear()

        for node in range(amount):
            self.head = self.head.next
            self._length -= 1

    def remove_tail(self, amount: int = 1) -> None:
        if self._length <= amount:
            self.clear()

        for node in range(amount):
            self.tail = self[-2]
            self.tail.next = None
            self._length -= 1

    def remove_at(self, index: int) -> None:
        if index < 0:
            index += self._length
        if not self._length > index >= 0:
            raise IndexError("Index out of range.")

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
            raise IndexError("Index out of range.")

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
        if self._length <= amount:
            self.clear()

        for node in range(amount):
            self.head = self.head.next
            self._length -= 1
            if self._length > 0:
                self.head.previous = None

    def remove_tail(self, amount: int = 1) -> None:
        if self._length <= amount:
            self.clear()

        for node in range(amount):
            self.tail = self.tail.previous
            self._length -= 1
            if self._length > 0:
                self.tail.next = None

    def remove_at(self, index: int) -> None:
        if index < 0:
            index += self._length
        if not self._length > index >= 0:
            raise IndexError("Index out of range")

        if index == 0:
            return self.remove_head()
        elif index == self._length - 1:
            return self.remove_tail()
        cursor = self[index].previous
        cursor.next = cursor.next.next
        cursor.next.previous = cursor
        self._length -= 1