def main() -> None:
    print("INPUT:")
    array: list[int] = list(map(int, input("Array: ").split()))

    print("\nOUTPUT:")
    print(array == array[::-1])


if __name__ == '__main__':
    main()