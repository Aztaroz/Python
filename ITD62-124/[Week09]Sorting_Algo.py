lst = []    #สร้าง List ว่าง

loop_num = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ : "))  #เก็บข้อมูลจำนวนครั้งที่ต้องการเรียงลำดับในตัวแปร loop_num

print("โปรดป้อนข้อมูลที่ต้องการเรียงลำดับ")
for a in range(loop_num):           #สร้าง Loop เพื่อจัดเก็บข้อมูลไว้ใน List
    data = int(input("ข้อมูล : "))
    lst.append(data)

print("ข้อมูลก่อนเรียงลำดับ คือ\n",*lst)   #แสดงผลข้อมูลก่อนเรียงลำดับ

for x in range(len(lst)):       #สร้าง Loop ให้ทำงานซ้ำเท่ากับจำนวนข้อมูลใน List
    for y in range(0, len(lst) -x -1):  #สร้าง Loop เพื่อเทียบค่าข้อมูลใน List ทีละชุด
        if lst[y] > lst[y+1]:
            tmp = lst[y]
            lst[y] = lst[y+1]
            lst[y+1] = tmp

print("ข้อมูลที่เรียงลำดับจากน้อยไปมาก คือ\n",*lst)       #แสดงผลข้อมูลหลังการเรียงลำดับแล้ว


#Hello From Ubuntu