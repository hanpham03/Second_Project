def NhapChieudai_va_Chieurong():
    chieudai = int(input("Nhap chieu dai:"))
    chieurong = int(input("Nhap chieu rong:"))
    return chieudai, chieurong


def TinhDT(chieudai, chieurong):
    return chieudai * chieurong


def TinhCV(chieudai, chieurong):
    return (chieudai + chieurong) * 2


def XuatDienTich(TinhDT, TinhCV):
    print("Dien tich hinh chu nhat", TinhDT)
    print("Chu vi hinh chu nhat", TinhCV)


def main():
    chieudai, chieurong = NhapChieudai_va_Chieurong()
    dientich = TinhDT(chieudai, chieurong)
    chuvi = TinhCV(chieudai, chieurong)
    In = XuatDienTich(chuvi, dientich)


if __name__ == "__main__":
    main()
