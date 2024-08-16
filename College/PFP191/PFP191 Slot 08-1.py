def sumev_while(n):
    s, r = 0, 0
    while s < n:
        r = r + s
        s = s + 2
    return n + r

def sumev_for(n):
    s = 0
    for i in range(2, n+1, 2):


def main():
    n = int(input("Nhập số: "))
    print("Kết quả của sumev_while:", sumev_while(n))
    print("Kết quả của sumev_for:", sumev_for(n))

if __name__ == '__main__':
    main()