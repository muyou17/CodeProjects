def main() -> None:
    print("INPUT:")
    hours: int = int(input("Hours: "))

    weeks, hours = divmod(hours, 168)
    days, hours = divmod(hours, 24)

    print("\nOUTPUT:")
    print("%d weeks, %d days, %d hours." % (weeks, days, hours))


if __name__ == '__main__':
    main()