#โปรแกรมรับค่าเลขท้าย 3 ตัวจากผู้ใช้งาน 10 คน
lotto_list = []     #!กำหนด List ว่าง
i = 0   #!เซ็ตค่า I เป็น 0 (เอาไว้นับจำนวนครั้ง)
while i<10:
    num = int(input())
    if len(str(num)) <= 3:  #!ตรวจสอบเงื่อนไขหากใส่ตัวเลขมาเกิน 3 ตัว
        lotto_list.append(num)  #!เพิ่มข้อมูลเข้าไปใน List
        i+=1    
    else:   #!เงื่อนไขหากป้อนตัวเลขมากกว่า 3 ตัว
        print("Input 3 Digit Number ONLY")