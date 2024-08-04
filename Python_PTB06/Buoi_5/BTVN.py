kwh = int(input("Nhập số kWh tiêu thụ: "))
cost = 0
if kwh >= 0:
    if kwh <= 50:
        cost = kwh*1700
    elif kwh <= 100:
        cost = 50*1700 + (kwh-50)*1900
    elif kwh <= 200:
        cost = 50*1700 + 50*1900 + (kwh-100)*2100
    else:
        cost = 50*1700 + 50*1900 + 100*2100 + (kwh-200)*3000
    print("Số tiền điện cần phải trả:",cost,end = " đồng")
else:
    print("Không hợp lệ",end = "")
