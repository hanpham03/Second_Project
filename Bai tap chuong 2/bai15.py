
s = input(">>").split()
if s[0] + s[1] < s[2] or s[0] + s[2] < s[1] or s[1] + s[2] < s[0]:
    print('ba dinh {}, {} va {} khong tạo thanh tam giac'.format(s[0], s[1], s[2]))
else:
    print('ba dinh {}, {} va {} co tạo thanh tam giac'.format(s[0], s[1], s[2]))