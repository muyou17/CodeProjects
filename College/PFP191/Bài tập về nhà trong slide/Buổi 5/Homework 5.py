from math import gcd


print("INPUT:")
a: str = input('a = ')
b: str = input('b = ')

print("\nOUTPUT:")
print(sum(1 for number in range(1, gcd(a, b)) if not gcd(a, b) % number))