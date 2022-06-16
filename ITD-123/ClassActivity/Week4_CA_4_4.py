from typing import Counter


#โปรแกรมคำนวณคะแนนเฉลี่ยนักเรียนที่คะแนนต่ำกว่า 9 คะแนน
score_lst = [3.6, 5.5, 8.7, 9.9, 10.0]  #! List ของคะแนนนักเรียน
count = 0   #! เซ็ตค่า count เป็น 0
sum = 0     #! เซ็ตค่า sum เป็น 0
for i in (score_lst):   #!ลูปคำนวณคะแนน
    if i < 9:      
        sum = sum + i
        count += 1
print("{:.2}".format(sum/count))