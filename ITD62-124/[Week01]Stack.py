def isFull (stack):   #สร้างฟังก์ชั่น isFull เพื่อตรวจสอบว่า List เต็มหรือไม่
    if len(stack) == stack_size:    # สร้างเงื่อนไขเพื่อตรวจสอบ
        print("-"*30)
        print("ไม่สามารถจัดเก็บข้อมูลใน Stack ได้เพราะ Stack เต็ม")
        print("-"*30)
        return True #ส่งค่า True กลับไป
    else:
        return False #ส่งค่า False กลับไป

def isEmpty (stack): #สร้างฟังก์ชั่น isEmpty เพื่อตรวจสอบว่า List ว่างหรือไม่
    if len(stack) == 0: # สร้างเงื่อนไขเพื่อตรวจสอบ
        print("-"*30)
        print("ไม่สามารถดึงข้อมูลออกจาก Stack เพราะไม่มีข้อมูลจัดเก็บใน Stack")
        print("-"*30)
        return True #ส่งค่า True กลับไป
    else:
        return False #ส่งค่า True กลับไป
        
def push(item): #สร้างฟังก์ชั่น push เพื่อเพิ่มค่าลงไปใน List
    if isFull(stack) == True: # สร้างเงื่อนไขเพื่อตรวจสอบ
        return True #ส่งค่า True กลับไป
    else:
        return stack.append(item) #เพิ่มข้อมูลลงใน List

def top(): #สร้างฟังก์ชั่น top เพื่อแสดงข้อมูลล่าสุดใน List
    if isEmpty(stack) == True: # สร้างเงื่อนไขเพื่อตรวจสอบ
        return
    else:
        print(stack[-1]) # ส่งค่า top กลับไป
        return
 
def pop(): #สร้างฟังก์ชั่น pop เพื่อข้อมูลใน List
    if isEmpty(stack) == True: # สร้างเงื่อนไขเพื่อตรวจสอบ
        return
    else:
        stack.pop() # ลบข้อมูลล่าสุดใน Stack

stack_input = False
main_loop = False
while stack_input == False: #สร้างลูปเพื่อวนซ้ำรับข้อมูล
    stack_size = int(input("โปรดระบุขนาดของ Stack ที่เป็นจำนวนเต็มที่มีค่ามากกว่า 0 : "))
    if stack_size >= 1:
        break #หากผ่านเงื่อนไขให้ Break ออกจากลูป
    elif stack_size <=0:
        stack_size = int(input("โปรดระบุขนาดของ Stack ที่เป็นจำนวนเต็มที่มีค่ามากกว่า 0 : "))
        
stack = []
while main_loop == False: # สร้างลูปเพื่อวนรับตัวเลือกผู้ใช้
    print("โปรดระบุทางเลือกในการดำเนินการกับ Stack\n1. PUSH\n2. POP\n3. Top of Stack\n4. Display ข้อมูลที่จัดเก็บใน Stack, ค่ามากที่สุด, ค่าน้อยที่สุด และค่าเฉลี่ยของข้อมูลที่จัดเก็บใน Stack")
    option = int(input("ทางเลือกในการดำเนินการ = "))
    if option == 1: # สร้างเงื่อนไขหากผู้ใช้เลือกเงื่อนไขที่ 1
        print("ทางเลือกในการดำเนินการ = 1")
        item = int(input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน Stack = "))
        push(item)
    elif option == 2: # สร้างเงื่อนไขหากผู้ใช้เลือกเงื่อนไขที่ 2
        print("ทางเลือกในการดำเนินการ = 2")
        pop()
            
    elif option == 3: # สร้างเงื่อนไขหากผู้ใช้เลือกเงื่อนไขที่ 3
        print("ทางเลือกในการดำเนินการ = 3")
        top()
    elif option == 4: # สร้างเงื่อนไขหากผู้ใช้เลือกเงื่อนไขที่ 4
        sum = 0
        print("#"*20)
        print("ทางเลือกในการดำเนินการ = 4")
        print(stack)
        print(max(stack))
        print(min(stack))
        for x in stack: # สร้างลูปเพื่อหาค่าเฉลี่ย
            sum = x + sum
            avg = sum / len(stack)
        print(avg)
        print("#"*20)
    else:
        break