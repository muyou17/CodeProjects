print("INPUT:")
k: int = int(input('k = '))

hundred: int = 0
while k >= 100:
    hundred += 1
    k -= 100

fifty: int = 0
while k >= 50:
    fifty += 1
    k -= 50

ten: int = 0
while k >= 10:
    ten += 1
    k -= 10

five: int = 0
while k >= 5:
    five += 1
    k -= 5

one: int = 0
while k >= 1:
    one += 1
    k -= 1

print("\nOUTPUT:")
print(f"Total: {hundred + fifty + ten + five + one}",
      f'$100: {hundred}', f'$50: {fifty}', f'$10: {ten}',
      f'$5: {five}', f'$1: {one}', sep='\n')