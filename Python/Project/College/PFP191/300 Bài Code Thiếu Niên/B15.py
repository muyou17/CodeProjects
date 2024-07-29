def main() -> None:
    print("INPUT:")
    day, month, year = map(int, input("Date: ").split())

    print("\nOUTPUT:")
    sum: int = int(30.42 * (month - 1)) + day
    if month == 2 or month > 2 and (not year % 400 or not year % 4 and year % 100):
        sum += 1
    if month in range(3, 8):
        sum -= 1
    print(sum)


if __name__ == '__main__':
    main()