def main() -> None:
    print("INPUT:")
    n: str = input('n = ')

    print("\nOUTPUT:")
    print(f'a) {sum(1 for number in map(int, list(n)) if not number % 2)}')
    print(f'b) {sum(map(int, list(n))) / len(n)}')
    print(f'c) {int(''.join(str(number) for number in map(int, list(n)) if not number % 2) or 0) + 1}')


if __name__ == '__main__':
    main()