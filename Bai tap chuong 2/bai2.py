def tinhToan(a, b, ch):
    if ch == '+':
        print(a, " + ", b, " = ", a + b)
    elif ch == '-':
        print(a, " - ", b, " = ", a - b)
    elif ch == '*':
        print(a, " * ", b, " = ", a * b)
    elif ch == '/':
        print(a, " / ", b, " = ", a / b)
    else:
        print(ch, ' không phải là một toán tử')
        return False

a = int(input("nhập một số nguyên: "))
b = int(input("nhập tiếp một số nguyên: "))
ch = str(input("Nhập một toán tử: "))
if (tinhToan(a, b, ch) == False):
    print("nhập lại: ")
    ch = str(input("Nhập một toán tử: "))
    tinhToan(a, b, ch)
