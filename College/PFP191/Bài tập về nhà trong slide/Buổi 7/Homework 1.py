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

    print("\nOUTPUT:")
    print(is_prime(n))


if __name__ == '__main__':
    main()