def main() -> None:
    print("INPUT:")
    array: list[int] = list(map(int, input().split()))

    print("\nOUTPUT:")
    print(array == sorted(array) if array else "The array is empty.")


if __name__ == '__main__':
    main()

