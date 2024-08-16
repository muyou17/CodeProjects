from math import isqrt


print("INPUT:")
n: int = int(input('n = '))

is_possible_prime: bool = True
if n <= 3:
    is_possible_prime = n > 1
else:
    for number in range(2, n):
        if not n % number:
            if number <= 3:
                is_prime = True
            elif not number % 2 or not number % 3:
                is_prime = False
            else:
                for integer in range(5, isqrt(number), 6):
                    if not number % integer or not number % (integer + 2):
                        is_prime = False
                        break
                else:
                    is_prime = True
            if not is_prime:
                is_possible_prime = False
                break

print("\nOUTPUT:")
print(is_possible_prime)