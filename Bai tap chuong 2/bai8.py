def docMotSo(n):
    if n == 0:
        return 'không'
    elif n == 1:
        return 'một'
    elif n == 2:
        return 'hai'
    elif n == 3:
        return 'ba'
    elif n == 4:
        return 'bốn'
    elif n == 5:
        return 'năm'
    elif n == 6:
        return 'sáu'
    elif n == 7:
        return 'bảy'
    elif n == 8:
        return 'tám'
    else:
        return 'chín'

n = int(input('nhập số nguyên từ 0 đến 9: '))
while n < 0 or n > 9:
    n = int(input('số nguyên từ 0 đến 9: '))

print('BẢNG CỬU CHƯƠNG', docMotSo(n).upper())
for i in range(1, 10):
    print('{} * {} = {}'.format(n, i, n*i))