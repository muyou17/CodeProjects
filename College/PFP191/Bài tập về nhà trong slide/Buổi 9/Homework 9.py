from itertools import filterfalse
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
    array: map = map(int, input("Array: ").split())

    print("\nOUTPUT:")
    print('array = %s' % list(filterfalse(is_prime, array)))


if __name__ == '__main__':
    main()