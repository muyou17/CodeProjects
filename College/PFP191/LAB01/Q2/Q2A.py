def q2(n):
    v = 1
    r = 0
    while v <= 4 * n:
        r = r + v
        v = v + 1
    return r

def main():
    n = int(input("Nhập n: "))
    print(q2(n))

if __name__ == '__main__':
    main()