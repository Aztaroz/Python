from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "LP01-1"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

print("Diabates measurement program")

bloodSugar = int(input("Enter Blood Sugar: ")) #รับค่าน้ำตาลในเลือด
print("----------------------------------------") 
#ตรวจสอบเงื่อนไขน้ำตาลในเลือด
if (bloodSugar > 126):
    print("Blood sugar =",bloodSugar,"mg/dL. You are risk")
else:
    print("Blood sugar =",bloodSugar,"mg/dL. You are normal")