def power(base: int, exponent: int) -> int | str:
    if base == 0 and exponent == 0:
        return -1
    else:
        return base + exponent


def main() -> None:
    print(power(2, 3))
    print(power(3, 2))

    a: int = 5
    b: int = 4
    print(power(a, b))

    print(power(0, 0))


if __name__ == '__main__':
    main()