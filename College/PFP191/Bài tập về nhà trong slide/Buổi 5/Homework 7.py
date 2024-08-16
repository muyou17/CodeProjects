from math import isqrt


print("INPUT:")
n: int = int(input('n = '))

for number in range(n - 1, 1, -1):
    if number <= 3:
        is_prime: bool = number > 1
    elif not number % 2 or not number % 3:
        continue
    else:
        for integer in range(5, isqrt(number), 6):
            if not number % integer or not number % (integer + 2):
                is_prime: bool = False
                break
        else:
            is_prime: bool = True
    if is_prime:
        smaller_prime: int = number
        break
else:
    smaller_prime = None

number: int = n
is_prime: bool = False
while not is_prime:
    number += 1
    if number <= 3:
        is_prime = number > 1
    elif not number % 2 or not number % 3:
        continue
    else:
        for integer in range(5, isqrt(number), 6):
            if not number % integer or not number % (integer + 2):
                break
        else:
            is_prime = True
    if is_prime:
        bigger_prime: int = number

print("\nOUTPUT:")
if bigger_prime - n < n - smaller_prime:
    print(bigger_prime)
else:
    print(smaller_prime)