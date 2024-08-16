def main() -> None:
    # Nhận input
    a, b = map(int, input("Input a, b: ").split())

    # Nếu a là 0
    if a == 0:
        # Nếu b cũng là 0 thì có vô số nghiệm
        if b == 0:
            x = '(-∞;+∞)'
        # Nếu b khác 0 thì vô nghiệm
        else:
            x = '∅'
    # Nếu a khác 0
    else:
        x = -b / a

    # In kết quả
    print('x =', x)


if __name__ == '__main__':
    main()