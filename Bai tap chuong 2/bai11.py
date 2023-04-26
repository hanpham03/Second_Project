#  s(x, n) = x  + x^2/2! + x^3/3! + ... + x^n/n!

def tinhGiaiThua(n):
    if (n==1 or n==0):
        return 1
    return n*tinhGiaiThua(n-1)

print("s(x, n) = x  + x^2/2! + x^3/3! + ... + x^n/n!")
n = int(input('nhap so nguyen n: '))
x = int(input('nhap so nguyen x: '))
s = 0
for i in range(1, n+1):
   s += (x**i)/tinhGiaiThua(i)
print("s= ", s)
