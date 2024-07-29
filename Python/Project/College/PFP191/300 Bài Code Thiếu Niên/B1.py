from math import pi, sqrt


def main() -> None:
    print("INPUT:")
    # Nhập diện tích S
    s: float = float(input('S = '))

    # Tính bán kính r
    r: float = sqrt(s / (4 * pi))

    print("\nOUTPUT:")
    # In ra thể tích V
    print('V =', 4 * pi * r ** 3 / 3)


if __name__ == '__main__':
    main()