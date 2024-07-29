def countLines(p):
    try:
        f = open(p, "r")
        return len(f.readlines())
    except:
        print("Không tìm được file")
        exit()
def main():
    p = input("Nhập file cần đếm số dòng: ")
    print(countLines(p))

if __name__ == "__main__":
    main()