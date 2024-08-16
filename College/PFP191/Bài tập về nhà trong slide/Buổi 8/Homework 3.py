def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))
    m: int = int(input('m = '))
    k: int = int(input('k = '))

    print("\nOUTPUT:")
    print(min(n, m) // k)


if __name__ == '__main__':
    main()