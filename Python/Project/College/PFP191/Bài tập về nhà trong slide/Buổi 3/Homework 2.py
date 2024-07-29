from math import isqrt


print("INPUT:")
n: int = int(input('n = '))

print("\nOUTPUT:")
if n <= 3:
    print(n > 1)
elif not n % 2 or not n % 3:
    print(False)
else:
    for number in range(5, isqrt(n), 6):
        if not n % number or not n % (number + 2):
            print(False)
            break
    else:
        print(True)