from itertools import chain, zip_longest
from sympy import isprime


def average_of_primes(a: int, b: int) -> int | str:
    if a > b: a, b = b, a
    primes: list[int] = list(filter(isprime, range(a, b + 1)))
    return sum(primes) / len(primes) if primes else "No prime in range."


def mix(a: int, b: int) -> str:
    if a < 0 or b < 0:
        return '-' + ''.join(chain.from_iterable(zip_longest(str(abs(a)), str(abs(b)), fillvalue='')))
    else:
        return ''.join(chain.from_iterable(zip_longest(str(a), str(b), fillvalue='')))


def main() -> None:
    print("INPUT:")
    a: int = int(input('a = '))
    b: int = int(input('b = '))

    print("\nOUTPUT:")
    print(f'1. {average_of_primes(a, b)}')
    print(f'2. {mix(a, b)}')


if __name__ == "__main__":
    main()