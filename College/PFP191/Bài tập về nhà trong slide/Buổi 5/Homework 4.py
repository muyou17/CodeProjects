print("INPUT:")
n: str = input('n = ')
k: str = input('k = ')


print("\nOUTPUT:")
print(sum(1 for digit in n if k == digit))