from linkedlists import SinglyLinkedList


def main() -> None:
    linked_list = SinglyLinkedList(6, 8, 2, 4)
    linked_list.sort()
    linked_list.traverse(0)


if __name__ == '__main__':
    main()