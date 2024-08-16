def q3(n, m):
    for i in range(0, n):
     print(m*'*')

def main():
    n = int(input("Nhập n: "))
    m = int(input("Nhập m: "))
    q3(n, m)

if __name__ == '__main__':
    main()