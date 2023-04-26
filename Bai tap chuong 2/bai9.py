n = int(input('nhập số nguyên dương: '))
while n < 0:
    n = int(input('số nguyên dương: '))

s1 = s2 = s3 = s4 = s5 = 0

# tính s1 = 1 + 2 + ... + n
for i in range (1, n+1):
    s1 += i
print('s1 = 1 + 2 + ... + {} = {}'.format(n, s1))

# tính s2 = 1 + 3 + ... + (2n - 1)
for i in range (1, 2*n):
    if i % 2 != 0:
        s2 += i
print('s2 = 1 + 3 + ... + (2n - 1) =', s2)

# tính s3 = 2 + 4 + ... + 2n
for i in range (2, (2*n)+1):
    if i % 2 == 0:
        s3 += i
print('s3 = 2 + 4 + ... + 2n =', s3)

# tính s4 = 1^2 + 2^2 + ... + n^2
for i in range (1, n+1):
    s4 += i*i
print('s4 = 1^2 + 2^2 + ... + n^2 = ', s4)

# tính s5 = 1/1 + 1/2 + ... +  1/n
for i in range (1, n+1):
    s5 += 1/i
print('s5 = 1/1 + 1/2 + ... +  1/n = ', s5)



