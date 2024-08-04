s = int(input("Số giây: "))
h = s//3600
ss = s-(h*3600)
m = ss//60
sss = ss-(m*60)
print("Chuyển đổi:",h,"giờ",m,"phút",sss,"giây",end="")