def nhapSoNguyen():
    x = int(input("nhập một số nguyên: "))
    return x

def kiemTraSoNguyenTo(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

# cau a bài 19
def tongTu1DenN(n):
    tong = 0
    for i in range(1, n+1):
        tong += i
    return tong

# cau b bài 19
def kiemTraCungLaSoNT(m, n):
    if kiemTraSoNguyenTo(m) == True and kiemTraSoNguyenTo(n) == True:
        print("hai số này cùng là số nguyên tố")
    else:
        print("hai số này không cùng là số nguyên tố")

# cau c bài 19
def secondsToTime(s):
    h = s//3600
    s = s % 3600
    m = s // 60
    s = s % 60
    print('{}h:{}m:{}s'.format(h, m, s))

# cau d bài 19
def giaTriTuyetDoi(a, b):
    return abs(a-b)

def main():
    n = nhapSoNguyen()
    # câu a
    print('tổng từ 1 đến ', n,' là: ', tongTu1DenN(n))
    # câu b
    a = nhapSoNguyen()
    b = nhapSoNguyen()
    kiemTraCungLaSoNT(a, b)
    # câu c
    s = int(input("nhập số giây để chuyển sang giờ: "))
    secondsToTime(s)
    # cau d
    c = nhapSoNguyen()
    d = nhapSoNguyen()
    print("giá trị tuyệt đối của a-b: ", giaTriTuyetDoi(c, d))

if __name__ == "__main__":
    main()