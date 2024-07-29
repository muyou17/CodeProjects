def is_happy(n: int, seen: set[int]):
    if n == 1:
        return True
    if n in seen:
        return False
    seen.add(n)
    return is_happy(sum(int(digit) ** 2 for digit in str(n)), seen)


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    print("\nOUTPUT:")
    print(is_happy(n, set()))


if __name__ == '__main__':
    main()