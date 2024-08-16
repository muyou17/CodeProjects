from math import sqrt


def main() -> None:
    print("INPUT:")
    # Nhập ba cạnh a b c
    a, b, c = map(float, input('Nhập a b c: ').split())

    # Tính chu vi P
    p: float = a + b + c

    print("\nOUTPUT:")
    # Kiểm tra độ dài từng cạnh
    if max(a, b, c) >= p - max(a, b, c):
        print("Độ dài các cạnh không hợp lệ.")
    # Nếu hợp lệ
    else:
        # Tính bán chu vi p
        p /= 2
        # In ra diện tích S
        print("S = %f" % sqrt(p * (p - a) * (p - b) * (p - c)))


if __name__ == '__main__':
    main()