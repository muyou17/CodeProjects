def denominator_count(n: int) -> int:
    return sum(1 for number in range(1, n + 1) if not n % number)


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    denominator_count_of_n: int = denominator_count(n)

    print("\nOUTPUT:")
    while True:
        n += 1
        if denominator_count_of_n == denominator_count(n):
            print('k = %d' % n)
            exit(0)


if __name__ == '__main__':
    main()