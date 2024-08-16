print("INPUT:")
a: int = int(input('a = '))
b: int = int(input('b = '))

while b:
    a, b = b, a % b

print("\nOUTPUT:")
print(a)