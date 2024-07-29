p = input('Chức vụ (M/E/G): ')

if p == 'M':
    mi = int(input('Lương cơ bản (₫): '))
    b = int(input('Phụ cấp (₫): '))
    print('Chức vụ của bạn là: Giám đốc')
    print('Lương của bạn là:', mi + b * 3, "₫")

if p == 'E':
    mi = int(input('Lương cơ bản (₫): '))
    t = int(input('Số giờ: '))
    print('Chức vụ của bạn là: Nhân viên')
    print('Lương của bạn là:', mi * t, "₫")

if p == 'G':
    mi = int(input('Lương cơ bản (₫): '))
    w = int(input('Số công: '))
    print('Chức vụ của bạn là: Bảo vệ')
    print('Lương của bạn là:', mi * w, "₫")

if p != ('M' and 'E' and 'G'):
    print('Bạn không phải là thành viên của công ty!')