def sum_of_denominators(n: int) -> int:
    return sum(filter(lambda number: not n % number, range(1, n + 1)))


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    a: int = sum_of_denominators(n)
    m: int = n + 1
    while sum_of_denominators(m) % a:
        m += 1

    print("\nOUTPUT:")
    print('m = %d' % m)


if __name__ == '__main__':
    main()