def primecheck(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n/2)):
            if n % i == 0:
                return False
                break
            else:
                return True

def main():
    n = int(input("Nhập số: "))
    if primecheck(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")

if __name__