def main() -> None:
    print("INPUT:")
    n: str = input('n = ')

    k: int = len(n)

    print("\nOUTPUT:")
    print(sum(int(digit) ** k for digit in n))


if __name__ == '__main__':
    main()