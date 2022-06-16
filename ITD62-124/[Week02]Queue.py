

class Queue():  
    def __init__(self,size):
        self.front = -1
        self.rear = -1
        self.queue = [None]*size
        self.size = size
    
    def enqueue(self,number):
        if self.rear == self.size -1:   #ตรวจสอบว่า Queue เต็มหรือไม่
            print("Queue เต็ม")
        else:
            if self.front == -1 and self.rear == -1:    #ตั้งเงื่อนไขหากจำนวน Element ของ Queue = -1  
                self.front = 0
                self.rear = 0
                self.queue[self.rear] = number              #todo
            else:
                self.rear += 1
                self.queue[self.rear] = number
        print("front =",self.front) #! Delete        
    def dequeue(self):  
        if self.front <= -1:            #ตั้งเงื่อนไขหาก Queue ว่าง
            print("Queue ว่าง")
        elif self.front > self.size -1:     #ตั้งเงื่อนไขหาก Queue ว่าง
            print("Queue ว่าง")
        else:
            print("front =",self.front) #! Delete
            self.queue[self.front] = None     #แทนที่จำนวนที่ลบไปด้วยคำว่า "none"
            self.front += 1        #ขยับ Index ของ Front ไป 1 ตำแหน่ง
    def display(self):
        if self.rear == -1:         #ตั้งเงื่อนไขหาก Queue ว่าง
            print("Queue ว่าง")
        else:    
            print(self.queue)
            #print("#####\nFront is",self.front,"\nRear is",self.rear,"\n#####")


queue_size = int(input("โปรดระบุขนาดของ Queue = "))
q = Queue(queue_size)

loop = True     #สร้างตัวแปรเพื่อใช้ควบคุมการ Loop
while loop == True:
    print("โปรดระบุทางเลือก\n"
            f"\t1. รับข้อมูลจำนวนเต็มจัดเก็บใน queue\n"
            f"\t2. ดึงข้อมูลจาก queue 1 ช่อง\n"
            f"\t3. แสดงข้อมูลที่จัดเก็บทั้งหมดใน queue ทางจอภาพ\n")
    choice = int(input("ทางเลือกในการดำเนินการ = "))

    if choice == 1:
        add_queue = int(input("ข้อมูลที่ต้องการเก็บข้อมูลใน queue = "))
        q.enqueue(add_queue)
        print("ข้อมูลที่ต้องการเพิ่ม :",add_queue)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    else:
        if q.rear == -1: #สร้างเงื่อนไขหาก Queue ว่าง
            print("ไม่สามารถแสดงผลรวม และจำนวนตัวเลขจำนวนเต็มที่มีค่ามากกว่า 200 ได้เพราะ Queue ว่าง")
        else:
            sum = 0  #กำหนดตัวแปรเพื่อบวกสะสมค่า
            for x in q.queue:
                if type(x) == int:      #ตรวจสอบว่าชนิดข้อมูลใน Queue เป็นตัวเลขหรือไม่
                    sum += x                #หากเป็นตัวเลขให้นำมาบวกสะสมค่าในตัวแปร sum
            count = 0                #สร้างตัวแปรเพื่อนับเลขจำนวนเต็มที่มีค่ามากกว่า 200
            for x in q.queue:
                if type(x) == int:
                    if x > 200:
                        count += 1
            print(sum)
            print("จำนวนตัวเลขจำนวนเต็มที่มีค่ามากกว่า 200 =",count)
        print("จบการทำงาน")
        break


