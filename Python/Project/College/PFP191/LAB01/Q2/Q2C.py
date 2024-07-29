def q2(n):
    v = 1
    r = 1
    while v <= n:
        r = r * v
        v = v + 2
    return r

def main():
    n = int(input("Nhập n: "))
    print(q2(n))

if __name__ == '__main__':
    main()