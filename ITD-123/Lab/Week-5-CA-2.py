from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "LP03-1-2"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

std_gpa_lst = []        #สร้าง List ว่าง
for i in range(10):     # *ใช้ For Loop เพื่อรับข้อมูล GPAX ของนักเรียนทั้ง 10 คน
    std_gpa_lst.append(float(input("Enter GPAX of Student No.{}: ".format(i+1))))       # *รับค่า GPAX ทาง Keyboard
print(std_gpa_lst)
print("-----------------------")
print("Average of GPAX: {:.3}".format((std_gpa_lst[1]+std_gpa_lst[2]+std_gpa_lst[4])/3))    #หาค่าเฉลี่ยของเกรดเฉลี่ยของนักเรียนลำดับที่ 2,3,5
max = std_gpa_lst[0]
min = std_gpa_lst[0]
for i in std_gpa_lst:       #*ใช้ For Loop เพื่อหาค่า GPAX ที่มากที่สุดและน้อยที่สุด
    if (i > max):
        max = i
    elif (i < min):
        min = i
print("Max GPAX:",max)
print("Min GPAX :",min)
