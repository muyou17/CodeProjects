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


def is_perfect(n: int) -> bool:
    return n == sum(filter(lambda number: not n % number, range(1, n)))


def average(n: int) -> float:
    sum: int = 0
    count: int = 0
    for number in range(1, n + 1):
        if is_prime(number) or is_perfect(number):
            sum += number
            count += 1
    return sum / count


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    print("\nOUTPUT:")
    print(average(n))


if __name__ == '__main__':
    main()