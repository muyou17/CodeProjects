def main() -> None:
    print("INPUT:")
    year: int = int(input("Năm sinh: "))

    print("\nOUTPUT:")
    match year % 12:
        case 1:
            print("Dậu")
        case 2:
            print("Tuất")
        case 3:
            print("Hợi")
        case 4:
            print("Tý")
        case 5:
            print("Sửu")
        case 6:
            print("Dần")
        case 7:
            print("Mão")
        case 8:
            print("Thìn")
        case 9:
            print("Tỵ")
        case 10:
            print("Ngọ")
        case 11:
            print("Mùi")
        case 12:
            print("Thân")


if __name__ == '__main__':
    main()