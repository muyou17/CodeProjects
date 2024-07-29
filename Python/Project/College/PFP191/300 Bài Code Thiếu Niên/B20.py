def price(electricity: float) -> int:
    if electricity < 100:
        return 500
    elif electricity < 250:
        return 800
    elif electricity < 350:
        return 1000
    else:
        return 1500


def main() -> None:
    print("INPUT:")
    electricity: float = float(input("Electricity (kWh): "))

    print("\nOUTPUT:")
    print("Bill (₫): %d" % round(electricity * price(electricity)))


if __name__ == '__main__':
    main()