def q1(a, x):
    return a * x ** 2

def main():
    x = float(input("Nhập x: "))
    a = float(input("Nhập a: "))
    print(q1(a, x))

if __name__ == '__main__':
    main()