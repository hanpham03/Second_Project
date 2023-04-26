from math import *
a = float(input('nhập hệ số a: '))
while a<=0:
    a = float(input('a phải lớn hơn 0: '))
b = float(input('nhập hệ số b: '))
c = float(input('nhập hệ số c: '))

delta = b*b - 4*a*c

if delta < 0:
    print('phương trình {}x^2 + {}x + {} = 0 vô nghiệm'.format(int(a), int(b), int(c)))
elif delta == 0:
    print('phương trình {}x^2 + {}x + {} = 0 có nghiệm kép'.format(int(a), int(b), int(c)))
    print('x1 = x2 = ', (-b)/2*a)
else:
    print('phương trình {}x^2 + {}x + {} = 0 có 2 nghiệm phân biệt'.format(int(a), int(b), int(c)))
    print('x1 = ', (-b + sqrt(delta)) /2 * a)
    print('x2 = ', (-b - sqrt(delta)) / 2 * a)