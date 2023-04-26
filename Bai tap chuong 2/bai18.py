def nhapSoNguyen():
    x = int(input("nhập một số nguyên: "))
    return x

def kiemTraSoNguyenTo(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def tongCacUocSoNT(n):
    tong = 0
    for i in range(1, n+1):
        if n%i == 0 and kiemTraSoNguyenTo(i)==True:
            tong += i
    return tong

def tongCacUocSoThuc(n):
    tong = 0.1
    for i in range(1, n, 0.1):
        if float(n) % i == 0:
            tong += i
    return tong - 0.1

def tongX2(n):
    tong = 0
    for i in range(12, n+1, 10):
        tong += i
    return tong

def main():
    n = nhapSoNguyen()
    print('tổng các ước số nguyên tố của ', n,'là: ', tongCacUocSoNT(n))
    # print('tổng các ước số thực của ', n, 'là: ', tongCacUocSoThuc(n))
    print('12 + 22 + 32 + ... + n với n= ', n, 'là: ', tongX2(n))

if __name__ == "__main__":
    main()

