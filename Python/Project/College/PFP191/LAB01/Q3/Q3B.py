def q3(n):
    v = 1
    while v <= n:
        print(v*'*')
        v = v + 1

def main():
    n = int(input("Nhập n: "))
    q3(n)

if __name__ == '__main__':
    main()