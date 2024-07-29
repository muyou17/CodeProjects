from math import factorial


def s(n: float) -> float:
    if n == 1:
        return 1
    else:
        return sum(range(n)) / factorial(n) + s(n - 1)


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    print("\nOUTPUT:")
    print(s(n))


if __name__ == '__main__':
    main()