from math import sqrt


def main() -> None:
    print("INPUT:")
    # Nhập điểm A
    xA, yA = map(float, input('A = ').split())
    # Nhập điểm B
    xB, yB = map(float, input('B = ').split())

    print("\nOUTPUT:")
    # In ra khoảng cách |AB|
    print('|AB| = %f' % sqrt((xB - xA) ** 2 + (yB - yA) ** 2))


if __name__ == '__main__':
    main()