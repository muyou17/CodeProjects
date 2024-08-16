def prtstr(d:str, s:int):
    return d[::s]

def revstr(d:str):
    return d[::-1]

d = input("Nhập dữ liệu: ")
s = int(input("Nhập số bước: "))

print(prtstr(d, s))