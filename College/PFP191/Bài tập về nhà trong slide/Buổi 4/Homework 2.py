print("INPUT:")
n: int = int(input('n = '))

denominator_count_of_n: int = 0
for number in range(1, n + 1):
    if not n % number:
        denominator_count_of_n += 1

print("\nOUTPUT:")
for m in range(n - 1, 0, -1):
    denominator_count_of_m: int = 0
    for number in range(1, m + 1):
        if not m % number:
            denominator_count_of_m += 1
    if denominator_count_of_m == denominator_count_of_n:
        print(m)
        break
else:
    print(-1)