n = int(input("nhập số nguyên: "))
while n<0:
    n = int(input('n phai lon hon 0: '))

def doi(n):
    i = 0
    s = ''
    while n != 0:
        c = n % 2
        n = n // 2
        i += 1
        s += str(c)
    return s[::-1]

print('so nhị phân của {} la {}'.format(n, doi(n)))