def prtevchar(s:str):
    for i in range(len(s)):
        if i % 2 == 0:
            print(s[i])

def main():
    s = input("Nhập chuỗi: ")
    prtevchar(s)

if __name__ == "__main__":
    main()