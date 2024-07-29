from math import cos, radians


def main() -> None:
    print("INPUT:")
    degree: float = int(input('x = ')) / 60 % 360

    print("\nOUTPUT:")
    if degree < 90:
        print("x thuộc góc vuông thứ 1")
    elif degree < 180:
        print("x thuộc góc vuông thứ 2")
    elif degree < 270:
        print("x thuộc góc vuông thứ 3")
    elif degree < 360:
        print("x thuộc góc vuông thứ 4")

    print(f'cos({radians(degree)}) = {cos(radians(degree))}')


if __name__ == '__main__':
    main()