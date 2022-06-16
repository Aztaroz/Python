#Elevetor Controller Program
from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "Quiz-2"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

print("Elevetor controller program...\n-------------------------------------------")
weight = []     #ตั้ง List ว่างขึ้นมา
total_weight = 0    # Set ค่าตัวแปรน้ำหนักรวมเป็น 0
for i in range (0,15):  #สร้าง Loop  เพื่อวนซ้ำรับค่าน้ำหนักจำนวน 15 คน
    weight.append(int(input("Enter peron {} weight: ".format(i+1))))    #รับค่าน้ำหนักไปเก็บไว้ใน List ของตัวแปร weight
    total_weight =  total_weight + weight[i]    #คำนวณหาน้ำหนักรวม
    if weight[i] == 0:  #ตั้งเงื่อไขว่าถ้าหากระบุค่า 0 จะทำหยุดการทำงานของ Loop
        i-=1
        break
    if total_weight > 1200: #ตั้งเงื่อนไขหยุดการทำงานของ Loop หากมีน้ำหนักรวมกันเกินกว่า 1200 KG
        print("-------------------------------------------")
        print("Warning:")
        print("Person {} is Over weight, Please leave....".format(i+1))
        print("Door closed, {} person(s), Total weight {} KG.".format(i,total_weight-weight[i]))
        break
if total_weight < 1200: #ตั้งเงื่อนไขเพื่อแสดงว่าประตูลิฟต์ปิดแล้ว มีจำนวนคนในลิฟต์เท่าไหร่ และ น้ำหนักรวมเท่าไหร่
    print("-------------------------------------------")
    print("Door closed, {} person(s), Total weight {} KG.".format(i+1,total_weight))

    