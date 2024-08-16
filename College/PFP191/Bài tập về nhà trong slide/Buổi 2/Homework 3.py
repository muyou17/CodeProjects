print("INPUT:")
a: int = int(input('a = '))
b: int = int(input('b = '))
operator: str = input("Operator: ")

print("\nOUTPUT:")
match operator:
    case '+':
        print(f'{a} + {b} = {a + b}')
    case '-':
        print(f'{a} - {b} = {a - b}')
    case '*':
        print(f'{a} × {b} = {a * b}')
    case '/':
        print(f'{a} ÷ {b} = {a / b}')
    case '//':
        print(f'{a} // {b} = {a // b}')
    case '%':
        print(f'{a} % {b} = {a % b}')
    case _:
        print("Invalid operator.")