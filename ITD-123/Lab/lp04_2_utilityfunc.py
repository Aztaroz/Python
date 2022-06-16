def validate_person_id (id):    #ประกาศฟังก์ชั่นชื่อ validate_person_id
    sum = 0
    count = 0
    length = len(id)            #กำหนดตัวแปร length ให้เท่ากับความยาวของตัวแปร id
    for i in range (0,12):              #ทำการวนซ้ำ 12 รอบ เพื่อหาผลการคูณ,บวก,Modulus
        sum_pos = int(i) * length
        sum = sum_pos + sum
        mod_result = sum % 11
        chk_digit = mod_result - 11 
        chk_digit = abs(chk_digit)      
        count+=1
        length-=1
    if chk_digit > 9:           #สร้างเงื่อนไขตรวจสอบขึ้นมาหาก Check Digit มีค่ามากว่า 9
        chk_digit = chk_digit % 10
        if chk_digit == int(id[12]):    #สร้างเงื่อนไขเพื่อใช้ตรวจสอบ Check Digit กับเลชท้าย Citizen id
            print("Return True")
            return True
    else:
        if chk_digit == int(id[12]):    #สร้างเงื่อนไขเพื่อใช้ตรวจสอบ Check Digit กับเลชท้าย Citizen id
            print("Return True")
            return True
        else:
            print("Return False")
            return False

def get_email():                            #ประกาศฟังก์ชั่นชื่อ get_email
    mail = input("Input your email : ")     #รับ Input Email จากผู้ใช้
    find_ch_chk = mail.find("@")            #สร้างตัวแปรเพื่อเก็บค่า Index ของตัว @
    ch_count = mail.count("@")              #สร้างตัวแปรเพื่อเก็บค่าจำนวนตัว '@' ในข้อความ
    dot_find = mail.find(".")               #สร้างตัวแปรเพื่อเก็บค่า Index ของตัว .
    dot_count = mail.count(".")             #สร้างตัวแปรเพื่อเก็บค่าจำนวนตัว '.' ในข้อความ               
    if find_ch_chk == 0:                #สร้างเงื่อนไขเพื่อตรวจสอบว่ามีการใส่ '@' เป็นตัวแรกของข้อความหรือไม่
         return get_email()             
    if ch_count == 0:                   #สร้างเงื่อนไขเพื่อตรวจสอบว่ามีการใส่ '@' ในข้อความหรือไม่
        return get_email()
    if ch_count >= 2:                   #สร้างเงื่อนไขเพื่อตรวจสอบว่ามีการใส่ '@' มากกว่า 1 ตัวในข้อความหรือไม่
        return get_email()
    if dot_count == 0:                  #สร้างเงื่อนไขเพื่อตรวจสอบว่ามีการใส่ '.' ในข้อความหรือไม่
        return get_email()
    if dot_find == find_ch_chk +1:      #สร้างเงื่อนไขเพื่อตรวจสอบว่ามีการใส่ '.' หลัง '@' หรือไม่ 
        return get_email()
    return mail




#print(get_email())
#validate_person_id("1234567890121")

#1234567890121


'''
def validate_person_id (id):
    sum_pos = 0
    for i in range (0,12):
        sum_pos += (int(id[i]) * (13-i))
    mod_result = sum_pos % 11
    chk_digit = abs(mod_result - 11)
    print(chk_digit)
    chk_result = chk_digit % 10
validate_person_id("1234567890121")
'''





#!Original
'''def validate_person_id (id):
    sum = 0
    count = 0
    length = len(id)
    for i in range (0,12):
        sum_pos = int(i) * length
        print(type(id))
        sum = sum_pos + sum
        mod_result = sum % 11
        chk_digit = mod_result - 11 

        print(i,"*",length,"=",sum_pos)
        print(sum_pos,"+",sum,"=",sum)
        
        chk_digit = abs(chk_digit)
        count+=1
        length-=1
    print(":::::::::::::::::::::::::")   
    print("ID is :",id)
    print("Count is :",count)
    print("Sum is :",sum)
    print("Mod_Result is :",mod_result)
    print("Check Digit is :", chk_digit)
    #print("Check Result is :",chk_result)

    if chk_digit > 9:
        chk_digit = chk_digit % 10
        print("Check Result is :",chk_digit,"& id[12] is :",id[12],"Data type id is :",type(id))
        if chk_digit == int(id[12]):
            print("Condition is True")
        return True
    else:
        if chk_digit == int(id[12]):
            print("Condition is True")
        else:
            print("Condition is false")
        return False

def get_email():
    mail = input("Input your email : ")
    find_ch_chk = mail.find("@")
    ch_count = mail.count("@")
    dot_find = mail.find(".")
    dot_count = mail.count(".")
    dot_chk = mail.find("@")
    if find_ch_chk == 0:
         return get_email()
    if ch_count == 0:
        return get_email()
    if ch_count >= 2:
        return get_email()
    if dot_count == 0:
        return get_email()
    if dot_find == dot_chk +1:
        return get_email()
    return mail
    '''