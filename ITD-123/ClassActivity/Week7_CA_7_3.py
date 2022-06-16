name = input("Enter name :")            #รับค่า Input มาเก็บไว้ที่ตัวแปรชื่อ name
age = input("Enter age : ")             #รับค่า Input มาเก็บไว้ที่ตัวแปรชื่อ avg
symp = input("Enter symptoms : ")       #รับค่า Input มาเก็บไว้ที่ตัวแปรชื่อ symp

def info(name ,age ,symp):              #ประกาศฟังก์ชั่นชื่อ Info เพื่อแสดงผลออกทางหน้าจอ
    print(name+"\n"+age+"\n"+symp)

info(name, age, symp)                   #เรียกใช้ฟังก์ชั่น Info