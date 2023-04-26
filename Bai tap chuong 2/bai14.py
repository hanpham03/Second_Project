print('bạn đi du lịch vào ngày thứ 4. sau n ngày bạn về là ngày:')
n = int(input('n= '))

if (n % 7 == 0 ):
    print(' thứ 4')
elif n % 7 == 1:
    print(' thứ năm')
elif n % 7 == 2:
    print(' thứ sáu')
elif n % 7 == 3:
    print(' thứ bảy')
elif n % 7 == 4:
    print(' chủ nhật')
elif n % 7 == 5:
    print(' thứ hai')
elif n % 7 == 6:
    print(' thứ ba')