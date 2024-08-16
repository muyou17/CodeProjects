from math import isqrt


print("INPUT:")
a: int = int(input('a = '))
b: int = int(input('b = '))

print("\nOUTPUT:")
for n in range(a, b + 1):
    if n <= 3:
        is_prime: bool = n > 1
    elif not n % 2 or not n % 3:
        is_prime: bool = False
    else:
        for number in range(5, isqrt(n), 6):
            if not n % number or not n % (number + 2):
                is_prime: bool = False
                break
        else:
            is_prime: bool = True

    if is_prime:
        print(n, end=' ')