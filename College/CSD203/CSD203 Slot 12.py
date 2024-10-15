from linkedlists import SinglyLinkedList, DoublyLinkedList


def main() -> None:
    linked_list = DoublyLinkedList(6, 8, 2, 4)
    linked_list.sort()
    linked_list.traverse()


if __name__ == '__main__':
    main()