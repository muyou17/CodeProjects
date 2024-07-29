def cntnum(s:str):
    c = 0
    for i in range(len(s)):
        if s[i] in '0123456789':
            c = c + 1
    return c

def main():
    s = input("Nhập chuỗi: ").strip()
    print(cntnum(s))

if __name__ == "__main__":
    main()