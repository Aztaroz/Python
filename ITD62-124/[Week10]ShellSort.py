def shell_sort(lst, num):   # สร้างฟังก์ชั่น shell_sort
    flag = 1
    gap_size = num
    while flag == 1 or gap_size > 1:  # สร้าง While Loop เพื่อตรวจสอบค่าตัวแปร flag หรือ เปรียบเทียบ gap_size > 1
        flag = 0
        gap_size = int((gap_size + 1) / 2)
        for y in range (num - gap_size):    # สร้าง For Loop เพื่อวนซ้ำจำนวนครั้งในช่วง num - gap_size
            if lst[y + gap_size] < lst[y]:  # ใช้ฟังก์ชั่น if เพือ่เปรียบเทียบระหว่าง lst[y + gap_size] < gap_size
                temp = lst[y + gap_size]    # สลับตำแหน่ง
                lst[y + gap_size] = lst[y]
                lst[y] = temp
                flag = 0

data_amount = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ : "))
lst = []*data_amount    # สร้าง List โดยมีจำนวนช่องเท่ากับตัวแปร data_amount

for x in range(data_amount):    # สร้าง Loop เพื่อวนซ้ำรับข้อมูลจำนวนครั้งในช่วง data_amount
    data = input("ข้อมูล : ")
    lst.append(data)

print("ข้อมูลก่อนเรียงลำดับ คือ","\n",*lst)
shell_sort(lst, data_amount)       # เรียกใช้ฟังก์ชั่น shell_sort
print("ข้อมูลที่เรียงลำดับจากน้อยไปมาก คือ","\n",*lst)
