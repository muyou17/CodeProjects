def writeFile(p):
    try:
        f = open(p, 'w')
        print("Nhập nội dung: ")
        l = input("> ")
        while l != "Done":
            f.write(l + "\n")
            l = input("> ")
        f.close()
    except:
        print("Không đọc được file")
        exit()
def readFile(p):
    try:
        f = open(p, "r")
        print(f.read())
        f.close()
    except:
        print("Không đọc được file")
        exit()

def main():
    print("Chương Trình Đọc-Ghi File")
    p = input("Nhập tên file cần ghi: ")
    writeFile(p)
    print("Dữ liệu trong file mới ghi là: ")
    readFile(p)

if __name__ == "__main__":
    main()