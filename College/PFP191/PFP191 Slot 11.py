def odd0(array):
    for i in range(1, len(array), 2):
        array[i] = 0
    return array

def rev(array):
    return array[::-1]

def sumfloat(array):
    for i in range(len(array)):
        if type(array[i]) == str:
            array.remove(array[i])
    return sum(array)

def main():
    array = []
    amount = int(input("Nhập số lượng phần tử: "))
    for i in range(amount):
        array.append(input("Nhập phần tử thứ " + str(i+1) + ":"))
    program = input("Chọn chương trình 1/2/3: ")
    while program != '1' and program != '2' and program != '3':
        print("Vui lòng chỉ nhập 1 hoặc 2 hoặc 3!")
    if program == '1':
        print(odd0(array))
    elif program == '2':
        print(rev(array))
    else:
        print(sumfloat(array))

if __name__ == '__main__':
    main()