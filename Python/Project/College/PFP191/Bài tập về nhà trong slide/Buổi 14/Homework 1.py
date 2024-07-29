from sympy import isprime


def largest_smaller_prime(n: int) -> int:
    for number in range(n - 1, 1, -1):
        if isprime(number):
            return number
    return 0


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    print("\nOUTPUT:")
    print(largest_smaller_prime(n) or "Not found.")


if __name__ == "__main__":
    main()