from math import factorial


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    print("\nOUTPUT:")
    for i in range(n):
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')
        print()


if __name__ == '__main__':
    main()