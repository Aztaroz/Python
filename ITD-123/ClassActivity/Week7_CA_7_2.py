temp = float(input("Input Temp : "))    #รับค่า Input มาเก็บไว้ที่ตัวแปร temp
def temp_bool(temp):                    #ประกาศฟังก์ชั่นชื่อ temp_bool เพื่อตรวจสอบเงื่อนไข
    if temp >= 37.5:
        result = True
    else:
        result = False
    return result





'''
if temp_bool(temp) == False:
    print("Come in")
else:
    print("Get out")
'''