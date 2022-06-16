#from Name import *
#Myname("LP02-1")

#ชื่อ
from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "LP02-1"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")
#################################################################################

print("Welcome to Exchange kiosk")
print("******************************************************")
rate = float(input("Today THB-USD exchange rate : "))   # รับ Exchange เป็น Float
usd = int(input("Enter $USD amount: ")) # รับ USD เป็น int
print("------------------------------------------------------")
thb = int(usd * rate)   # คำนวณเงินไทย 
fee = thb * 0.02        # คำนวณค่าธรรมเนียม
net = thb - fee         # คำนวณเงินสุทธิ
print(usd,"USD =",int(thb),"THB,","Fee = {:.2f}".format(fee),"\nNet",int(net),"THB")
print("------------------------------------------------------")
print("Bank note and coin:")

# ส่วนของการแบ่งธนบัตร/เหรียญ
banknote = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
for i in banknote:
    if net >= 20:
        print("Banknote {} : {}".format(i,int((net/i))))
    else:
        print("Coin {} : {}".format(i,int((net/i))))
    net %= i
print("------------------------------------------------------")
        

"""
exchange_rate = 0.00
usd = 0
thb = 0
fee = 0
total = 0

print("Welcome to Exchange kiosk")
exchange_rate = float(input("Today THB-USD exhcange rate: "))
usd = int(input("Enter $USD amount: "))
thb = int(usd*exchange_rate)
fee = thb*0.02
total = int(thb-fee)

txt = "{} USD = {} THB, Fee = {:.2f} THB"
print(txt.format(usd, thb, fee))


txt = "Net {} THB"
print(txt.format(total))

print("Bank note and coin:")
banknote1000 = int(total/1000)
total = total%1000
txt = "Bank note 1000 : {}"
print(txt.format(banknote1000))

banknote500 = int(total/500)
total = total%500
txt = "Bank note 500 : {}"
print(txt.format(banknote500))

banknote100 = int(total/100)
total = total%100
txt = "Bank note 100 : {}"
print(txt.format(banknote100))

banknote50 = int(total/50)
total = total%50
txt = "Bank note 50 : {}"
print(txt.format(banknote50))

banknote20 = int(total/20)
total = total%20
txt = "Bank note 20 : {}"
print(txt.format(banknote20))

coin10 = int(total/10)
total = total%10
txt = "Coin 1000 : {}"
print(txt.format(coin10))

coin5 = int(total/5)
total = total%5
txt = "Coin 5 : {}"
print(txt.format(coin5))

coin2 = int(total/2)
total = total%2
txt = "Coin 2 : {}"
print(txt.format(coin2))

coin1 = int(total/1)
total = total%1
txt = "Coin 1: {}"
print(txt.format(coin1))
"""