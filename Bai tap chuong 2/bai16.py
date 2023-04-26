def nhapDMY():
    day = int(input("nhập ngày: "))
    while day < 0 or day > 31:
        day = int(input("ngày > 0 và ngày < 32: "))

    month = int(input("nhập tháng: "))
    while month < 0 or month > 12:
        month = int(input("tháng > 0 và tháng < 13: "))

    year = int(input("nhập năm: "))
    while year < 1900:
        year = int(input("năm tính từ 1900 trở đi: "))

    return day, month, year

def kiemTraDate(d, m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        print('ngày', d, '/', m, '/', y, 'hợp lệ')
    elif m  == 2:
        if y % 400 == 0 or (y%4==0 and y%100 != 0):
            if d > 29:
                print('ngày', d, '/', m, '/', y, 'không hợp lệ')
            else:
                print('ngày', d, '/', m, '/', y, 'hợp lệ')
        else:
            if d > 28:
                print('ngày', d, '/', m, '/', y, 'không hợp lệ')
            else:
                print('ngày', d, '/', m, '/', y, 'hợp lệ')
    else:
        if d > 30:
            print('ngày', d, '/', m, '/', y, 'không hợp lệ')
        else:
            print('ngày', d, '/', m, '/', y, 'hợp lệ')

def main():
    d, m, y = nhapDMY()
    kiemTraDate(d, m, y)


if __name__ == "__main__":
    main()
