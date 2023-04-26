def main():
    r = float(input('nhập bán kính: '))
    print('chu vi hình tròn bán kính {} là {}'.format(r, tinhCV(r)))
    print('diện tích hình tròn bán kính {} là {}'.format(r, tinhDT(r)))

def tinhCV(r):
    return 2 * 3.14 * r

def tinhDT(r):
    return 3.14 * r * r

if __name__ == "__main__":
    main()