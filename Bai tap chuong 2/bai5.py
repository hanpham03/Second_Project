n = int(input("nhập số nguyên có tối đa 2 chữ số: "))
while n<0 or n>99:
    n = int(input("nhập lại số nguyên có tối đa 2 chữ số: "))

def docMotSo(n):
    if n == 1:
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
    elif n == 9:
        return 'chín'
    else:
        return 'không'

if (n < 10):
    print(docMotSo(n))
else:
    a = int(n / 10)
    b = int(n % 10)
if a == 1 and b == 5:
    print('mười lăm')
elif a == 1 and b != 5:
    print('mười', docMotSo(b))
elif b == 5 and a != 1:
    print('{} mươi lăm'.format(docMotSo(a)))
else:
    print('{} mươi {}'.format(docMotSo(a), docMotSo(b)))
