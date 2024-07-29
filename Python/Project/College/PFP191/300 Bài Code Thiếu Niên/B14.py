def tomorrow(day: int, month: int, year: int) -> str:
    match month:
        case 2:
            if not year % 400 or not year % 4 and year % 100:
                if day < 29:
                    return f'{day + 1:02}/{month:02}/{year}'
                else:
                    return f'01/03/{year}'
            else:
                if day < 28:
                    return f'{day + 1:02}/{month:02}/{year}'
                else:
                    return f'01/03/{year}'
        case 12:
            if day < 31:
                return f'{day + 1:02}/{month:02}/{year}'
            else:
                return f'01/01/{year + 1}'
        case 4 | 6 | 9 | 11:
            if day < 30:
                return f'{day + 1:02}/{month:02}/{year}'
            else:
                return f'01/{month + 1:02}/{year}'
        case _:
            if day < 31:
                return f'{day + 1:02}/{month:02}/{year}'
            else:
                return f'01/{month + 1:02}/{year}'


def yesterday(day: int, month: int, year: int) -> str:
    if day > 1:
        return f'{day - 1:02}/{month:02}/{year}'

    match month:
        case 1:
            return f'31/12/{year - 1}'
        case 3:
            if not year % 400 or not year % 4 and year % 100:
                return f'29/02/{year}'
            else:
                return f'28/02/{year}'
        case 5 | 7 | 10 | 12:
            return f'30/{month - 1:02}/{year}'
        case _:
            return f'31/{month - 1:02}/{year}'


def main() -> None:
    print("INPUT:")
    day, month, year = map(int, input("Today: ").split())

    print("\nOUTPUT:")
    print(f"Tomorrow: {tomorrow(day, month, year)}")
    print(f"Yesterday: {yesterday(day, month, year)}")


if __name__ == '__main__':
    main()