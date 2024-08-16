from datetime import timedelta


def main() -> None:
    print("INPUT:")
    hour, minute, second = map(int, input("From: ").split())
    earlier: timedelta = timedelta(hours=hour, minutes=minute, seconds=second)
    hour, minute, second = map(int, input("To: ").split())
    later: timedelta = timedelta(hours=hour, minutes=minute, seconds=second)

    print("\nOUTPUT:")
    print("Distance:", later - earlier)


if __name__ == '__main__':
    main()