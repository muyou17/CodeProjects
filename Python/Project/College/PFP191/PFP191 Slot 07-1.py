def prtstring(d, o):
    if o == "even":
        l = d[1::2]
    elif o == "odd":
        l = d[::2]
    print(l)

def main():
    d = input("Nhập chuỗi ký tự: ")
    o = input("Nhập thứ tự (odd/even): ")
    prtstring(d, o)

if __name__ == '__main__':
    main()