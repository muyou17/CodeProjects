def countChar(p):
    try:
        f = open(p, "r")
        return len(f.read())
    except:
        print("Không tìm được file")
        exit()
def main():
    p = input("Nhập file cần đếm ký tự: ")
    print(countChar(p))

if __name__ == "__main__":
    main()