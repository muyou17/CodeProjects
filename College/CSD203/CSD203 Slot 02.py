class Rectangular:
    def __init__(self, x: float, y: float) -> None:
        self.length = x
        self.width = y

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self) -> None:
        print("Chiều dài:", self.length,
              "\nChiều rộng:", self.width,
              "\nChu vi:", self.perimeter(),
              "\nDiện tích:", self.area())

def print_perimeter_sum(rectangulars: list[Rectangular]) -> float:
    sum = float()
    for element in rectangulars:
        sum += Rectangular.perimeter(element)
    return sum

def print_area_sum(rectangulars: list[Rectangular]) -> float:
    sum = float()
    for element in rectangulars:
        sum += Rectangular.area(element)
    return sum

def main() -> None:
    rectangulars = list()
    for index in range(5):
        x, y = map(float, input().split())
        rectangulars.append(Rectangular(x, y))

    #Print all elements
    for rectangular in rectangulars:
        Rectangular.display(rectangular)

    #Print sum of perimeters:
    print(sum([Rectangular.perimeter(rectangular) for rectangular in rectangulars]))
    
    #Print min of areas:
    print(min([Rectangular.area(rectangular) for rectangular in rectangulars]))


if __name__ == '__main__':
    main()