def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    print("\nOUTPUT:")
    print(n == sum(filter(lambda number: not n % number, range(1, n))))


if __name__ == '__main__':
    main()