from linkedlists import DoublyLinkedList


def main() -> None:
    li = [4, 7, 6, 2, 5]
    linked_list = DoublyLinkedList(3, 4)
    linked_list += DoublyLinkedList(2, 1) + li
    del linked_list[-3]
    print(linked_list)


if __name__ == '__main__':
    main()