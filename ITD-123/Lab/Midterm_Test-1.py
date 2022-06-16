#Water Billing Program
from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "Quiz-1"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

print("Water billing program\n-------------------------------------------")
unit = int(input("Enter water unit(s): "))      #รับค่า unit จากคีย์บอร์ด
cost = 0        # Set ค่าตัวแปร Cost เป็น 0
if unit <= 15:      # ส่วนของเงื่อนไขในการคำนวณค่าน้ำ
    cost = 10       # Set ค่าตัวแปร Cost ตามเงื่อนไขการคำนวณราคาของแต่ละเงื่อนไข
elif unit <= 30:
    cost = 15
elif unit > 30:
    cost = 20
print("Total cost = {}".format(unit*cost+30))   # คำนวณและแสดงผลลัพธ์