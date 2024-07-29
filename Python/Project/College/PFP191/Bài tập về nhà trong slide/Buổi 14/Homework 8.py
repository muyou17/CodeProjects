def decode(s: list[str]) -> filter:
    denominators: list[int] = list(filter(lambda number: not len(s) % number, range(2, len(s))))
    return filter(lambda index: any(not index % number for number in denominators), range(len(s)))


def main() -> None:
    print("INPUT:")
    s: list[str] = input('s = ').split()

    print("\nOUTPUT:")
    print(*(s[index] for index in decode(s)))


if __name__ == '__main__':
    main()