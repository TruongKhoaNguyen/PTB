password = "Doraemon"   # Có thể thay đổi
type_in = input("Vui lòng nhập mật khẩu : ")
while not (type_in == password):
    print("Mật khẩu không chính xác")
    type_in = input("Vui lòng nhập lại mật khẩu : ")
print("Đăng nhập thành công",end="")
