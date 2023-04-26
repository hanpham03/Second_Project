month = int(input("Nhập vào một tháng: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print ("tháng {} có 31 ngày".format(month))
elif month in [4, 6, 9, 11]:
    print("tháng {} có 30 ngày".format(month))
elif month == 2:
    year = int(input("Nhập thêm năm: "))
    if (year%400==0 | (year%4==0 & year%100!=0)):
        print("tháng {} có 29 ngày".format(month))
    else:
        print("tháng {} có 28 ngày".format(month))