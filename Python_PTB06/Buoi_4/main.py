print("A game from HTLO-PTB06")
print("Chào mừng đến với trò chơi Euro Lư Hương Vàng 2024")
print("Luật chơi :")
print("- Dự đoán đội đã dành chiến thắng")
print("- Đúng +3, Sai -2, Đoán lụi -5")
print("Có tổng cộng 10 trận đấu")
point = 0
#Cau_1
print("Trận 1 : Germany - Scotland")
print("1. Germany ; 2. Scotland")
tl1 = int(input("Bạn chọn : "))
if tl1 == 1:
    point += 3
    print("GOAL !!!")
    print("Điểm (+3) :",point,end = "")
elif tl1 == 2:
    point -= 2
    print("MISS :)")
    print("Điểm (-2) :",point,end = "")
else:
    point -= 5
    print("KHÔNG HỢP LỆ >:(")
    print("Điểm (-5) :",point,end = "")
#Cau_2
print("Trận 2 : Hungary - Switzerland")
print("1. Hungary ; 2. Switzerland")
tl2 = int(input("Bạn chọn : "))
if tl2 == 2:
    point += 3
    print("GOAL !!!")
    print("Điểm (+3) :",point,end = "")
elif tl2 == 1:
    point -= 2
    print("MISS :)")
    print("Điểm (-2) :",point)
else:
    point -= 5
    print("KHÔNG HỢP LỆ >:(")
    print("Điểm (-5) :",point,end = "")
#Cau_3
print("Trận 3 : Spain - Croatia")
print("1. Spain ; 2. Croatia")
tl3 = int(input("Bạn chọn : "))
if tl3 == 1:
    point += 3
    print("GOAL !!!")
    print("Điểm (+3) :",point,end = "")
elif tl3 == 2:
    point -= 2
    print("MISS :)")
    print("Điểm (-2) :",point)
else:
    point -= 5
    print("KHÔNG HỢP LỆ >:(")
    print("Điểm (-5) :",point,end = "")
#Cau_4
print("Trận 4 : Italy - Albania")
print("1. Italy ; 2. Albania")
tl4 = int(input("Bạn chọn : "))
if tl4 == 1:
    point += 3
    print("GOAL !!!")
    print("Điểm (+3) :",point,end = "")
elif tl4 == 2:
    point -= 2
    print("MISS :)")
    print("Điểm (-2) :",point)
else:
    point -= 5
    print("KHÔNG HỢP LỆ >:(")
    print("Điểm (-5) :",point,end = "")
#Cau_5
print("Trận 5 : Poland - Netherlands")
print("1. Poland ; 2. Netherlands")
tl5 = int(input("Bạn chọn : "))
if tl5 == 2:
    point += 3
    print("GOAL !!!")
    print("Điểm (+3) :",point,end = "")
elif tl5 == 1:
    point -= 2
    print("MISS :)")
    print("Điểm (-2) :",point)
else:
    point -= 5
    print("KHÔNG HỢP LỆ >:(")
    print("Điểm (-5) :",point,end = "")
#Cau_6
print("Trận 6 : Serbia - England")
print("1. Serbia ; 2. England")
tl6 = int(input("Bạn chọn : "))
if tl6 == 2:
    point += 3
    print("GOAL !!!")
    print("Điểm (+3) :",point,end = "")
elif tl6 == 1:
    point -= 2
    print("MISS :)")
    print("Điểm (-2) :",point)
else:
    point -= 5
    print("KHÔNG HỢP LỆ >:(")
    print("Điểm (-5) :",point,)
#Cau_6
print("Trận 7 : Romania - Ukraine")
print("1. Romania ; 2. Ukraine")
tl7 = int(input("Bạn chọn : "))
if tl7 == 1:
    point += 3
    print("GOAL !!!")
    print("Điểm (+3) :",point,end = "")
elif tl7 == 2:
    point -= 2
    print("MISS :)")
    print("Điểm (-2) :",point)
else:
    point -= 5
    print("KHÔNG HỢP LỆ >:(")
    print("Điểm (-5) :",point,end = "")