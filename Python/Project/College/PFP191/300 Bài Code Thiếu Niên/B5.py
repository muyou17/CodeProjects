def main() -> None:
    print("INPUT:")
    # Nhập tọa độ điểm A
    a: tuple[float, float] = tuple(map(float, input('A = ').split()))
    # Nhập tọa độ điểm B
    b: tuple[float, float] = tuple(map(float, input('B = ').split()))
    # Nhập tọa độ điểm C
    c: tuple[float, float] = tuple(map(float, input('C = ').split()))
    # Nhập tọa độ điểm M
    m: tuple[float, float] = tuple(map(float, input('M = ').split()))

    # Công thức tính diện tích tam giác từ tọa độ 3 điểm
    s = lambda a, b, c: abs(a[0] * b[1] - b[0] * a[1] + b[0] * c[1] -
                            c[0] * b[1] + c[0] * a[1] - a[0] * c[1]) / 2
    #Tính diện tích tam giác ∆ABC
    area: float = s(a, b, c)
    #Tính tổng diện tích các tam giác ∆MAB ∆MBC ∆MCA
    sum: float = s(m, a, b) + s(m, b, c) + s(m, c, a)

    print("\nOUTPUT:")
    # So sánh tổng các diện tích với diện tích tam giác ∆ABC
    if sum < area:
        print("M is inside the triangle.")
    elif sum > area:
        print("M is outside the triangle.")
    else:
        print("M is on an edge of the triangle.")


if __name__ == '__main__':
    main()