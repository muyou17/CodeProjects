def replace_all(d: str, o: str, b: str):
    d = d.replace(o, b)
    return d

def replace_fn(d: str, o: str, b: str, n: int):
    return d.replace(o, b, n)

#def replace_ln(d: str, o: str, b: str, n: int):

def main():
    f = input("Hàm (all/fn/ln): ")
    if f == 'all' or f == 'fn' or f == 'ln':
        d = input("Chuỗi: ")
        o = input("Chuỗi cần thay thế: ")
        b = input("Chuỗi thay thế: ")
        if f == 'fn':
            n = int(input("Số lần thay thế: "))
            print(replace_fn(d, o, b, n))
        elif f == 'ln':
            n = int(input("Số lần thay thế: "))
            print(replace_ln(d, o, b, n))
        else:
            print(replace_all(d, o, b))
    else:
        print("Vui lòng chọn hàm All hoặc First n hoặc Last n")

if __name__ == "__main__":
    main()