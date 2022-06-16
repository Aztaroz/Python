''' def compare2num (num1, num2):
    if num1 > num2:
        print("num 1 is greater than num 2")
        return num1
    elif num2 > num1:
        print("num 2 is greater than num 1")
        return num2
    else:
        print("num1 and num2 is equal")
        return num1, num2
compare2num(20,10)
import numpy as np
def getGpax(student):
    gpaxList = []
    for x in range (student):
        gpax = input('gpax:')
        gpaxList.append(gpax)
    gpaxArray = np.array(gpaxList)
    return gpaxArray
print(getGpax(3))

def roomcost(hour):
    day = hour // 24    #คำนวณหาจำนวนวัน
    extra_hour = hour % 24  #คำนวนหาจำนวนชั่วโมงที่เกินมา
    cost = (day * 2000) + (extra_hour * 150)    #คำนวณหาค่าห้องพัก
    return cost
    #print(day,"day",extra_hour,"hour","\nCost :",cost)
print(roomcost(50))
'''