from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "LP03-1-1"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

# ข้อ 1  สร้าง List สําหรับเก็บข้อมูลหมายเลขสายการบินที่จะลงจอดที่ท่าอากาศยานนครฯ 2 เที่ยวบิน คือ SL789 และ FD3187
flight_landing_lst = ["SL789","FD3187"]
print(flight_landing_lst)

#! ข้อที่ 2 เพิ่มเที่ยวบินรหัส DD7802 ใน List
flight_landing_lst.append(input("Enter flight no: "))
print(flight_landing_lst)

# ข้อที่ 3 ลบเที่ยวบิน SL789 ออกจาก List
flight_landing_lst.pop(0)
print(flight_landing_lst)

# ข้อที่ 4 เรียกดูข้อมูลในรายการลําดับที่ 2
print(flight_landing_lst[1])

# ข้อที่ 5 เรียกดูข้อมูลในรายการลําดับที่ 1
print(flight_landing_lst[0])

# ข้อที่ 6 แก้ไขข้อมูลเที่ยวบินลําดับที่ 1 จาก FD3187 เป็น FD3188 และแสดงผลข้อมูลที่จัดเก็บไวใน List
flight_landing_lst[0] = "FD3188"
print(flight_landing_lst)

#! ข้อที่ 7 เพิ่มข้อมูลเที่ยวบินใหม่ที่กําลังเดินทางมาอีกจํานวน 2 เที่ยวบิน คือ TG789 และ SL790 และแสดงผลข้อมูลที่จัดเก็บไวใน List
flight_landing_lst.append(input("Enter flgiht no: "))
flight_landing_lst.append(input("Enter flight no: "))
print(flight_landing_lst)

#! ข้อที่ 8 ลบข้อมูลเที่ยวบิน TG789 และแสดงผลข้อมูลที่จัดเก็บไวใน List
flight_landing_lst.remove(input("Enter flight no. to remove: "))
print(flight_landing_lst)

# ข้อที่ 9 ทำการเคลียร์ข้อมูลของ List
flight_landing_lst.clear()
print(flight_landing_lst)