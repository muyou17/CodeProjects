from math import sqrt, isqrt


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    elif not n % 2 or not n % 3:
        return False
    for number in range(5, isqrt(n), 6):
        if not n % number or not n % (number + 2):
            return False
    else:
        return True


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    s: float = 0
    index: int = 0
    number: int = 2
    while index < n:
        if is_prime(number):
            index += 1
            s += index / sqrt(number)
        number += 1

    print("\nOUTPUT:")
    print(s)


if __name__ == '__main__':
    main()