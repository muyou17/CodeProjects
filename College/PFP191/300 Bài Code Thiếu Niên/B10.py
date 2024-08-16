def validate(sin: str) -> bool:
    if len(sin) != 9 or not sin.isdecimal():
        return False

    s1: int = sum(int(sin[index]) for index in range(0, 7, 2))
    s2: int = sum(sum(divmod(int(sin[index]) * 2, 10)) for index in range(1, 8, 2))
    return not (s1 + s2 + int(sin[-1])) % 10


def main() -> None:
    while True:
        sin: str = input('SIN: ')
        if sin == '0':
            exit(0)
        else:
            print("Valid SIN." if validate(sin) else "Invalid SIN.", end='\n\n')


if __name__ == '__main__':
    main()