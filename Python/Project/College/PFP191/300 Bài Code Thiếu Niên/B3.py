def main() -> None:
    print("INPUT:")
    # Nhập tọa độ tâm C
    xC, yC = map(float, input('C = ').split())
    # Nhập bán kính r
    r: float = float(input('r = '))
    # Nhập tọa độ điểm M
    xM, yM = map(float, input('M = ').split())

    # Tính bình phương khoảng cách từ C đến M |CM|²
    squared_distance: float = (xM - xC) ** 2 + (yM - yC) ** 2

    print("\nOUTPUT:")
    # Nếu |CM|² nhỏ hơn r² thì M nằm trong hình tròn
    if squared_distance < r * r:
        print("M is inside the circle.")
    # Nếu |CM|² lớn hơn r² thì M nằm ngoài hình tròn
    elif squared_distance > r * r:
        print("M is outside the circle.")
    # Nếu |CM|² bằng r² thì M nằm trên đường tròn
    else:
        print("M is on the circumference.")


if __name__ == '__main__':
    main()