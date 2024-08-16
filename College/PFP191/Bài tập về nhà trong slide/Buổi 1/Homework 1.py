from math import sqrt


print("INPUT:")
a: float = float(input('a = '))
b: float = float(input('b = '))
c: float = float(input('c = '))

p: float = (a + b + c) / 2

print("\nOUTPUT:")
print('S = %f' % sqrt(p * (p - a) * (p - b) * (p - c)))