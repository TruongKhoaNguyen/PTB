print("Nhập vào chiều cao của 03 bạn: ")
an = int(input("An: "))
minh = int(input("Minh: "))
lan = int(input("Lan: "))
if an>minh and an>lan:
    print("Bạn cao nhất là: An",end="")
elif minh>an and minh>lan:
    print("Bạn cao nhất là: Minh",end="")
elif lan>an and lan>minh:
    print("Bạn cao nhất là: Lan",end="")