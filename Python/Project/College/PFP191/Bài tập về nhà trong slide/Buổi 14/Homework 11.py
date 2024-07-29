def main() -> None:
    print("INPUT:")
    hex: str = input('Hexadecimal: ')

    print("\nOUTPUT:")
    print(f'Decimal: {int(hex, 16)}')


if __name__ == "__main__":
    main()