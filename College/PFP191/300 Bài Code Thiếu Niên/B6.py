def main() -> None:
    # Nhận input
    a, b, c = map(int, input("Input a, b, c: ").split())

    # a phải nhỏ hơn b
    if a > b:
        b, a = a, b

    # b phải nhỏ hơn c
    if b > c:
        b, c = c, b

    # In kết quả
    print("Ascending:", a, b, c)


if __name__ == '__main__':
    main()