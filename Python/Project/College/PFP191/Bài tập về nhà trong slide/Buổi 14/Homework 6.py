from math import sqrt, isqrt


def main() -> None:
    print("INPUT:")
    n: int = int(input('n = '))

    array: list[int] = []
    number: int = n
    while len(array) < n:
        if sqrt(number) == isqrt(number):
            array.append(number)
        number += 1

    print("\nOUTPUT:")
    print(array)


if __name__ == '__main__':
    main()