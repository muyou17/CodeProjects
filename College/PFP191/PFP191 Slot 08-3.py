def cntvow(s:str):
    s = s.lower()
    c = 0
    for i in range(len(s)):
        if s[i] in 'ueoai':
            c = c + 1
    return c

def main():
    s = input("Nhập chuỗi: ").strip()
    print(cntvow(s))

if __name__ == "__main__":
    main()