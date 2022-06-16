from datetime import date, datetime
now  = datetime.now()
print("-------------------------------------------")
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "Lab Quiz 4"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

import numpy as np
data_arr = np.array([[70,75,80,88,72,92],
                    [99,101,80,85,79,82],
                    [100,89,95,120,122,99]])
day = 0
for row in data_arr:
    time = 1
    sum = 0
    print("Day :",day+1)
    for collumn in row:
        sum = sum + collumn
        print("Times#{} : {}".format(time,collumn))
        time += 1
    print("Average : {:.1f}".format(sum/6))
    print("--------------------")
    day += 1




'''
for x in range (0,3):
    sum = 0
    print("Day {} :".format(x+1))
    for y in range(0,6):
        sum = sum + data_arr[x,y]
        print("Times#{} : {}".format(y+1,data_arr[x,y]))
    print("Average : {:.1f}".format(sum/6))
    print("--------------------")
'''
