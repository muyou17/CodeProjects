from re import findall


def main() -> None:
    print("INPUT:")
    s: str = input('s = ')

    print("\nOUTPUT:")
    print(len(set(map(int, findall(r'\d+', s)))))


if __name__ == "__main__":
    main()