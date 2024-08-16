def q4(l):
    return round((sum(l))/len(l), 4)

def main():
    l = []
    n = int(input("- Số lượng phần tử: "))
    print("- Danh sách:")
    d = 1
    for i in range(0, n):
        l.append(float(input("  + Phần tử thứ " + str(d) + ": ")))
        d = d + 1
    print(q4(l))

if __name__ == '__main__':
    main()