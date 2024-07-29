from functools import lru_cache
from math import sqrt, isqrt


@lru_cache
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci(n: int) -> None:
    for number in range(n + 1):
        print(fibonacci(number), end=' ')
    print()


def is_perfect_square(n: int) -> bool:
    return sqrt(n) == isqrt(n)


def is_fibonacci(n: int) -> bool:
    n = 5 * n ** 2
    return is_perfect_square(n + 4) or is_perfect_square(n - 4)


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    print("\nOUTPUT A:")
    print_fibonacci(n)

    print("\nOUTPUT B:")
    print(is_fibonacci(n))


if __name__ == '__main__':
    main()