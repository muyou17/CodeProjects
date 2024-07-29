def gcd(x, y):
    z = 1
    if x < y: x, y = y, x
    for i in range(y, 0, -1):
        if x % i == 0 and y % i == 0:
            z = i
            break
    return z

x = int(input("Số thứ nhất: "))
y = int(input("Số thứ hai: "))

print("Ước chung lớn nhất của", x, "và", y, "là:", gcd(x, y))