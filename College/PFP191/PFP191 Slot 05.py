c = input("Nhập 6 ký tự: ")

if len(c) != 6:
    print("Vui lòng nhập đúng 6 ký tự!")

else:

    a = c[0]
    b = c[1]
    c = c[2]
    d = c[3]

    if a == 'a' or 'e' or 'i' or 'o' or 'u':
        a = 'x'
    elif a == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        a = 'y'
    else:
        a = 'z'

    if b == 'a' or 'e' or 'i' or 'o' or 'u':
        b = 'x'
    elif b == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        b = 'y'
    else:
        b = 'z'

    if a == 'a' or 'e' or 'i' or 'o' or 'u':
        a = 'x'
    elif a == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        a = 'y'
    else:
        a = 'z'