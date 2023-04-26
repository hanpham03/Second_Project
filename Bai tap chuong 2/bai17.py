# s1 = 1 + 2 + ... + 2n
def tong1(n):
    s1 =0
    for i in range(1, 2*n+1):
        s1 += i
    return s1

def tongLe(n):
    s2 = 0
    for i in range(1, n):
        if i%2 != 0:
            s2 += i
    return s2

def tongChan(n):
    s3 = 0
    for i in range(1, n):
        if i%2 == 0:
            s3 += i
    return s3

def main():
    n = int(input("nhập số tự nhiên n= "))
    print('1 + 2 + ... + 2n = ', tong1(n))
    print('tổng các số lẽ < ',n,': ', tongLe(n))
    print('tổng các số chẵn < ', n, ': ', tongChan(n))

if __name__ == '__main__':
    main()