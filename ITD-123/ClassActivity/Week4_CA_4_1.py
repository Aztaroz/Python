#*การเพิ่ม-ลบข้อมูลนักเรียนใน List

lst = ["Jessy", "Ammy", "Luzy", "Jenny", "John"]    #!สร้าง List เพื่อเก็บข้อมูล

print(lst[1])   #!เรียกใช้ข้อมูล Ammy

lst.append("BigBoss")   #!เพิ่มข้อมูล BigBoss ใน List

print(*lst[2:5]) #!แสดงชื่อสมาชิกเฉพาะ Luzy,Jenny,John

print(*lst[0:2])    #!แสดงชื่อสมาชิกเฉพาะ Jessy, Ammy

lst.pop(3)      #!ลบข้อมูล Jenny ออกจาก List