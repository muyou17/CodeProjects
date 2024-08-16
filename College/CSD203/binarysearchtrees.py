from functools import total_ordering
from collections.abc import Iterable


@total_ordering
class Node:
    """Node of Binary Search Tree"""

    def __init__(self, data: int, left=None, right=None) -> None:
        self.data: int = data
        self.left: Node | None = left
        self.right: Node | None = right

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.data == other.data
        elif isinstance(other, int):
            return self.data == other
        else:
            return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Node):
            return self.data < other.data
        elif isinstance(other, int):
            return self.data < other
        else:
            return NotImplemented


@total_ordering
class BSTree:
    """Binary Search Tree"""

    def __init__(self, *data: Node | int | Iterable[Node | int]) -> None:
        self.root = None
        if data:
            self.insert(data)

    def __add__(self, data: Node | Iterable[Node | int]):
        if not isinstance(data, Node | Iterable):
            return NotImplemented
        self.insert(data)
        return self

    def __len__(self) -> int:
        return self.node_count(self.root)

    def __eq__(self, other) -> bool:
        if not isinstance(other, BSTree | Iterable):
            return NotImplemented
        return self.node_count(self.root) == len(other)

    def __lt__(self, other) -> bool:
        if not isinstance(other, BSTree | Iterable):
            return NotImplemented
        return self.node_count(self.root) < len(other)

    def min(self, parent: Node | None = None) -> int:
        if not parent:
            parent = self.root

        if not parent:
            return None

        current: Node = self.root
        while current.left:
            current = current.left
        return current.data

    def max(self, parent: Node | None = None) -> int:
        if not parent:
            parent = self.root

        if not parent:
            return None

        current: Node = parent
        while current.right:
            current = current.right
        return current.data

    def height(self, parent: Node | None = -1) -> int:
        """Height of the binary search tree."""

        if parent == -1:
            parent = self.root

        if not parent or not parent.left and not parent.right:
            return 0

        return 1 + max(self.height(parent.left), self.height(parent.right))

    def node_count(self, parent: Node | None = -1) -> int:
        """Counts the nodes in the binary search tree."""

        if parent == -1:
            parent = self.root

        if not parent:
            return 0

        return 1 + self.node_count(parent.left) + self.node_count(parent.right)

    def leaf_count(self, parent: Node | None = -1) -> int:
        """Counts the leaves in the binary search tree."""

        if parent == -1:
            parent = self.root

        if not parent:
            return 0

        if not parent.left and not parent.right:
            return 1

        return self.leaf_count(parent.left) + self.leaf_count(parent.right)

    def insert(self,
               *data: Node | int | Iterable[Node | int],
               parent: Node | None = None) -> Node | None:
        """Inserts data into the binary search tree."""

        if not parent:
            parent = self.root

        for item in data:
            if isinstance(item, Iterable):
                for subitem in item:
                    self.insert(subitem, parent=parent)
            else:
                if isinstance(item, int):
                    item = Node(item)

                if self.root:
                    self.__insert(item, parent)
                else:
                    self.root = item
        return self.root

    def remove(self, data: Node | int, parent: Node | None = None) -> None:
        """Removes data from the binary search tree."""

        if not parent:
            parent = self.root

        if isinstance(data, int):
            data = Node(data)

        self.__remove(data, parent)

    def preorder(self, parent: Node | int | None = None) -> list[int]:
        """Returns a list of integers representing the preorder traversal of the binary search tree."""

        if not parent:
            parent = self.root
        tree_preorder: list[int] = []

        def traverse(node: Node | None):
            if not node:
                return None
            tree_preorder.append(node.data)
            traverse(node.left)
            traverse(node.right)

        if isinstance(parent, int):
            parent = Node(parent)

        traverse(parent)
        return tree_preorder

    def inorder_display(self, parent: Node | None = None) -> None:
        """Displays the inorder (LNR) traversal of the binary search tree."""

        self.__inorder(parent if parent else self.root)
        print()

    def postorder_display(self, parent: Node | None = None) -> None:
        """Displays the postorder (LRN) traversal of the binary search tree."""

        self.__preorder(parent if parent else self.root)
        print()

    def __insert(self, node: Node | int, parent: Node) -> None:
        """Helper function to insert a node into the binary search tree."""

        if node.data < parent.data:
            if parent.left:
                self.__insert(node, parent.left)
            else:
                parent.left = node
        elif node.data > parent.data:
            if parent.right:
                self.__insert(node, parent.right)
            else:
                parent.right = node

    def __remove(self, node: Node, parent: Node | None) -> Node | None:
        """Helper function to remove a node from the binary search tree."""

        if parent:
            if node.data < parent.data:
                parent.left = self.__remove(parent.left, node)
            elif node.data > parent.data:
                parent.right = self.__remove(parent.right, node)
            else:
                if not parent.left:
                    return parent.right
                if not parent.right:
                    return parent.left

                min_larger_node: Node = self.min(parent.right)
                parent.data = min_larger_node.data
                parent.right = self.__remove(parent.right, min_larger_node)
        return parent

    def __preorder(self, parent: Node | None) -> None:
        if parent:
            print(parent, end=' ')
            self.__preorder(parent.left)
            self.__preorder(parent.right)

    def __inorder(self, parent: Node | None) -> None:
        if parent:
            self.__inorder(parent.left)
            print(parent, end=' ')
            self.__inorder(parent.right)

    def __postorder(self, parent: Node | None) -> None:
        if parent:
            self.__postorder(parent.left)
            self.__postorder(parent.right)
            print(parent, end=' ')