def first_degree(a: int, b: int) -> None:
    if a == 0:
        if b == 0:
            x = '(-∞;+∞)'
        else:
            x = '∅'
    else:
        x = -b / a
    print('x =', x)


def main() -> None:
    # Nhận input
    a, b, c = map(int, input("Nhap a, b, c: ").split())

    # Nếu là phương trình bậc nhất
    if a == 0:
        first_degree(b, c)

    # Nếu là phương trình bậc hai
    else:
        # Tính delta
        Δ = b ** 2 - 4 * a * c

        # Nếu delta âm thì vô nghiệm
        if Δ < 0:
            x1 = '∅'
            x2 = '∅'

        # Nếu delta không âm thì có hai nghiệm
        else:
            x1 = (-b + Δ ** 0.5) / (2 * a)
            x2 = (-b - Δ ** 0.5) / (2 * a)

        # In kết quả
        print('x₁ =', x1)
        print('x₂ =', x2)



if __name__ == '__main__':
    main()