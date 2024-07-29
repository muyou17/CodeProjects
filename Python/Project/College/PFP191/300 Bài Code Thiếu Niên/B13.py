def day_of_week(day: int, month: int, year: int) -> str:
    days: tuple = ("Saturday", "Sunday", "Monday", "Tuesday",
                   "Wednesday", "Thursday", "Friday")

    if month in (1, 2):
        month += 12
        year -= 1

    j, k = divmod(year, 100)
    return days[(day + 13 * (month + 1) // 5 + k
                 + k // 4 + j // 4 - 2 * j) % 7]


def validate(day: int, month: int, year: int) -> bool:
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 0 < day <= 31
        case 4 | 6 | 9 | 11:
            return 0 < day < 31
        case 2:
            if not year % 400 or not year % 4 and year % 100:
                return 0 < day <= 29
            else:
                return 0 < day < 29
        case _:
            return False


def main() -> None:
    print("INPUT:")
    day, month, year = map(int, input("Date: ").split())

    print("\nOUTPUT:")
    print("Valid date.\n%s" % day_of_week(day, month, year)
          if validate(day, month, year) else "Invalid date.")


if __name__ == '__main__':
    main()