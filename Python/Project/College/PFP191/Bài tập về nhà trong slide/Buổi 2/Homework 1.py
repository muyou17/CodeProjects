print("INPUT:")
a: int = int(input('a = '))
b: int = int(input('b = '))
c: int = int(input('c = '))

print("\nOUTPUT:")
if not a:
    if b:
        x = -c / b
    elif c:
        x = '∅'
    else:
        x = '(-∞;+∞)'
    print(f'x = {x}')
else:
    Δ = b ** 2 - 4 * a * c
    if Δ < 0:
        x1 = '∅'
        x2 = '∅'
    else:
        x1 = (-b + Δ ** 0.5) / (2 * a)
        x2 = (-b - Δ ** 0.5) / (2 * a)
    print(f'x₁ = {x1}\nx₂ = {x2}')