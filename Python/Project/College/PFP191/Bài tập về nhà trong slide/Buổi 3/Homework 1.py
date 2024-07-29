print("INPUT:")
n: int = int(input('n = '))

sum: int = 0
for number in range(1, n):
    if not n % number:
        sum += number

print("\nOUTPUT:")
print(sum)