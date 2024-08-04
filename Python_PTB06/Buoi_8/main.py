p_list = ["PS5","Window 11","Xbox","iPhone 15 ProMax","Mac_book"]
price = [50000000,72000000,68500000,114320000,138610000]
ymoney = 1000000000
items = ["PS5"]
itemscost = [50000000]
while True:
    print("1. Để ra menu.")
    print("2. Để mua.")
    print("3. Thêm hàng vào giỏ")
    print("4. Thêm hàng vào cửa hàng")
    print("5. Ăn hàng trong cửa hàng")
    print("6. Ăn hàng trong giỏ")
    print("Nhập sai trừ 5000000")
    n = int(input("Nhập ở đây --> "))
    if n == 1:
        print("=====TRUNG TÂM BÁN HÀNG LẬU=====")
        for i in range(len(p_list)):
            print("==",p_list[i],"-",price[i],"$")
        x = input()
    elif n == 2:
        print("Bạn đang có (hàng fake): ")
        for i in range(len(items)):
            print("==",items[i])
        x = input()
    elif n == 3:
        print("Bạn có (hàng fake): ")
        for i in range(len(items)):
            print("==",items[i])
        n = int(input("Nhập hàng bạn muốn mua (bắt đầu từ 0): "))
        items.append(p_list[n])
        itemscost.append(price[n])
        print("Đã ghiền món hàng và cho vào giỏ",p_list[n])
        x = input()
    elif n == 4:
        print("=====TRUNG TÂM BÁN HÀNG LẬU=====")
        for i in range(len(p_list)):
            print("==",p_list[i],"-",price[i],"$")
        p_listinclude = input("Nhập hàng muốn bán: ")
        priceinclude = int(input("Bạn muốn bán với giá bao nhiêu $: "))
        p_list.append(p_listinclude)
        price.append(priceinclude)
        print("Đã giục",p_listinclude,"với mức giá",priceinclude)
        x = input()
    elif n == 5:
        print("=====TRUNG TÂM BÁN HÀNG LẬU=====")
        for i in range(len(p_list)):
            print("==",p_list[i],"-",price[i],"$")
        delete = int(input("Nhập hàng muốn ăn (bắt đầu tại 0): "))
        print("Chúc ngon miệng. Ăn :",p_list[delete])
        p_list.pop(delete)
        price.pop(delete)
        x = input()
    elif n == 6:
        print("Bạn có (hàng fake): ")
        for i in range(len(items)):
            print("==",items[i])
        delete = int(input("Nhập hàng muốn ăn (bắt đầu tại 0): "))
        print("Chúc ngon miệng. Ăn :",items[delete])
        items.pop(delete)
        itemscost.pop(delete)
        x = input()
    elif n == 7:
        print("=====TRUNG TÂM BÁN HÀNG LẬU=====")
        for i in range(len(p_list)):
            print("==",p_list[i],"-",price[i],"$")
        changed = int(input("Nhập hàng muốn sửa giá: "))
        newprice = int(input("Nhập giá mới của: " + p_list[i]))
        price[changed] = newprice
        print("Đã sửa giá")
        x = input()
    elif n == 8:
        destroy_choose = input("BCMXHTCNGTGHCBHK (Y/N) ?")
        if destroy_choose == "Y":
            items.clear()
            print("Đã xóa :(")
            x = input()
        elif destroy_choose == "N":
            x = input()
        else:
            ymoney -= 5000000
            x = input()
    elif n == 9:
        tongcong = 0
        for gia in itemscost:
            tongcong += gia
        ymoney -= tongcong
        print("Bạn đã mua các hàng giả sau:",items,"với tổng tiền là",tongcong)
        print("Số tiền còn lại here:",ymoney)
        print("Đây là hàng giả của bạn. Nếu có vấn đề thì tự giải quyết")
        items.clear()
        x = input()




