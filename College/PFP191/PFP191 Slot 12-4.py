def formula(n):
    v = n
    s = 0
    while v < 2 * n:
        s = s + 1/v**0.5
        v = v + 1
    return s

def main():
    n = int(input("Enter number: "))
    print("OUTPUT:")
    print(formula(n))

if __name__ == '__main__':
    main()