from math import isqrt


print("INPUT:")
n: int = int(input('n = '))

print("\nOUTPUT:")
is_prime: bool = False
while not is_prime:
    n += 1
    if n <= 3:
        is_prime = n > 1
    elif not n % 2 or not n % 3:
        continue
    else:
        for number in range(5, isqrt(n), 6):
            if not n % number or not n % (number + 2):
                break
        else:
            is_prime = True
    if is_prime:
        print(n)