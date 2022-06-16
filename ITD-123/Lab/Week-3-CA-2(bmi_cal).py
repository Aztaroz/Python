from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "LP01-1"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

#โปรแกรมคำนวณ BMI
print("Body Mass Index (BMI) Calculator")
weight = float(input("Enter your weight(kg): "))    #รับค่าน้ำหนัก(กิโลกรัม)
height = float(input("Enter your height(M): "))     #รับค่าส่วนสูง(เมตร)
print("---------------------------------------")
bmi = weight/(height**2)    #คำนวณค่า BMI
result = ""   #ตัวแปรเอาไว้เก็บค่าผลลัพธ์ข้อความ
txt = "BMI = {:.2f}. You are {}"
#ตรวจสอบเงื่อนไข
if (bmi < 18.5):
    risk = "Underweight"
    print(txt.format(bmi,risk))
elif (bmi <= 24.9):
    risk = "Healthy"
    print(txt.format(bmi,risk))
elif (bmi <= 29.9):
    risk = "Overweight"
    print(txt.format(bmi,risk))
elif (bmi > 30.0):
    risk = "Obese"
    print(txt.format(bmi,risk))
print("---------------------------------------")