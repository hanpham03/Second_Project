n = int(input("nhap n= "))
s = 0
for i in range(1, n+1):
    s += i # s = s + i
print("tong tu 1 den ", n, " = ", s)
s1 = 1
for i in range(1, n+1):
    s1 *= i
print("tich tu 1 den ", n, " = ", s1)
