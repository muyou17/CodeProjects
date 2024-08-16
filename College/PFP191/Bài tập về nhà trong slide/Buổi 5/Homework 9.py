print("INPUT:")
h: int = int(input('h = '))

print("\nOUTPUT:")
for line in range(1, h + 1):
    if line == 1 or line == h:
        print('* ' * line)
    else:
        print('*' + '  ' * (line - 2) + ' *')