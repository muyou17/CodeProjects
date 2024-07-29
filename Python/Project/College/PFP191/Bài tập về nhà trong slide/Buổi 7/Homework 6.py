from math import isqrt


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
    index: int = 1
    number: int = 1
    while index < n:
        number += 1
        if is_prime(number):
            s += 1 / number
            index += 1

    print("\nOUTPUT:")
    print(s)


if __name__ == '__main__':
    main()