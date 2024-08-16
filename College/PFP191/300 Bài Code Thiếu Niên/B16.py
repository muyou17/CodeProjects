from calendar import prcal, day_name, weekday


def main() -> None:
    print("INPUT:")
    year = int(input("Year: "))

    print("\nOUTPUT:")
    prcal(year)
    print(f"01/01/{year} is {day_name[weekday(year, 1, 1)]}.")


if __name__ == '__main__':
    main()