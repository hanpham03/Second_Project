def nhapSoNguyen():
    x = int(input("nhập một số nguyên: "))
    return x

def kiemTraSoNguyenTo(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

# kiểm tra xem x có phải là ước chung của a và b không
def uocChung(x, a, b):
    if a % x ==0 and b % x == 0:
        return True
    return False

# kiểm tra so nguyên tố lớn nhất trong đoạn (m, n)
def kiemTraSNTLNTrongDoanMN(m, n):
    s = []
    for i in range(m, n+1):
        if kiemTraSoNguyenTo(i) == True:
            s.append(i)
    if len(s) == 0:
        return 0
    max = s[0]
    for j in range(1, len(s)):
        if s[j] > max:
            max = s[j]

    return max

def main():
    m = nhapSoNguyen()
    n = nhapSoNguyen()
    while n < m:
        print('n phải lớn hơn m: ')
        n = nhapSoNguyen()
    if kiemTraSNTLNTrongDoanMN(m, n) == 0:
        print("khong có số nguyên tố nào trong đoạn này!!")
    else:
        print('số nguyên tố lon nhất đồng thời là ước chung trong đoạn (', m, ',', n, ') là: ',
              kiemTraSNTLNTrongDoanMN(m, n))

if __name__ == "__main__":
    main()