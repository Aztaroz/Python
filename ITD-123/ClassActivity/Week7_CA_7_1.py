def avg(*num_lst):  #ประกาศฟังก์ชั่น avg เพื่อหาค่าเฉลี่ย
    sum = 0
    for i in num_lst:
        sum = i + sum
        ans = sum / len(num_lst)
    return ans
print(avg(20,30))   #เรียกใช้ฟังก์ชั่นและแสดงผลออกทางหน้าจอ









#number = [20,30]