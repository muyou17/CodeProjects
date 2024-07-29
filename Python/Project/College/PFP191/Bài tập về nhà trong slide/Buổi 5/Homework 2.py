print("INPUT:")
n: int = int(input('n = '))
k: int = int(input('k = '))

print("\nOUTPUT:")
print(sum(1 for number in range(1, n + 1) if not number % k))