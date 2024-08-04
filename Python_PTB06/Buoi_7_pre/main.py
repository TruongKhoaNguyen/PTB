a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
if a+b>c and a+c>b and b+c>a:
    if a==b or b==c or a==c:
        if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
            print("Tam giac vuong can")
        elif a==b==c:
            print("Tam giac deu")
        else:
            print("Tam giac can")
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
        if a!=b or b!=c or a!=c:
            print("Tam giac vuong")
    else:
        print("Tam giac")
else:
    print("Khong phai tam giac")



# print("Guess the number")
# print("***Nhap -1 de thoat")
# import random
# number = random.randint(0,1000)    #ngau nhien
# Num_input = int(input("Nhap so: "))
# while number != Num_input:
#     if Num_input == -1:
#         print(";(")
#         break
#     elif Num_input<0 or Num_input>1000:
#         print("WTF ARE YOU TYPING >:(")
#         Num_input = int(input("Nhap lai: "))
#         continue
#     if number > Num_input:
#         print("Bigger than",Num_input)
#     elif number < Num_input:
#         print("Smaller than",Num_input)
#     Num_input = int(input("Nhap lai: "))
# print("Good")



exit()      #khong chay chuong trinh
username = "Gooigi"
password = "nobita"
Account = input("Vui long nhap tai khoan: ")
Pass = input("Vui long nhap mat khau: ")
while not (Account == username and Pass == password):
    print("Dang nhap khong thanh cong")
    Account = input("Vui long nhap lai tai khoan: ")
    Pass = input("Vui long nhap lai mat khau: ")
print("Dang nhap thanh cong !!!")
print("Ban khong phai la gian diep :)",end="")