from fractions import Fraction


print("INPUT:")
a: int = int(input('a = '))
b: int = int(input('b = '))

fraction: Fraction = Fraction(a, b)

print("\nOUTPUT:")
print(fraction.numerator, fraction.denominator)