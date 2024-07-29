def main() -> None:
    print("INPUT:")
    a: int = int(input('a = '))
    b: int = int(input('b = '))
    operator: str = input("Operator: ")

    print("\nOUTPUT:")
    match operator:
        case '+':
            if b < 0:
                print(f'{a} + ({b}) = {a + b}')
            else:
                print(f'{a} + {b} = {a + b}')
        case '-':
            if b < 0:
                print(f'{a} + {-b} = {a - b}')
            else:
                print(f'{a} - {b} = {a - b}')
        case '*':
            if b < 0:
                print(f'{a} × ({b}) = {a * b}')
            else:
                print(f'{a} × {b} = {a * b}')
        case '/':
            if b > 0:
                print(f'{a} ÷ {b} = {a / b}')
            elif b < 0:
                print(f'{a} ÷ ({b}) = {a / b}')
            else:
                print("Error: Unable to divide by zero.")
        case '//':
            if b > 0:
                print(f'{a} // {b} = {a // b}')
            elif b < 0:
                print(f'{a} // ({b}) = {a // b}')
            else:
                print("Error: Unable to divide by zero.")
        case '%':
            if b > 0:
                print(f'{a} % {b} = {a % b}')
            elif b < 0:
                print(f'{a} % ({b}) = {a % b}')
            else:
                print("Error: Unable to modulo by zero.")
        case '**':
            if b < 0:
                print(f'{a} ↑ ({b}) = {a ** b}')
            else:
                print(f'{a} ↑ {b} = {a ** b}')


if __name__ == '__main__':
    main()