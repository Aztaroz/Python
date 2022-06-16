'''
class Node: #สร้าง Class Node ขึ้นมา
    def __init__(self,info = None):     #สร้าง Method ขึ้นมา
        self.info = info
        self.next = None
class LinkedList:   #สร้าง Class LinkedList ขึ้นมา
    def __init__(self):     #สร้าง Method __init__
        self.head = None
        self.tail = None
    def Add_Front_Data(self,data):  #สร้าง Method เพื่อเพิ่ม Node จากด้านหน้า
        if self.head != None:   #สร้างเงื่อนไขหากเคยสร้าง Node มาก่อนแล้ว
            add_node = Node(data)
            add_node.next = self.head
            self.head = add_node
        else:   #เพิ่มเงื่อนไขกรณีที่ยังไม่เคยสร้าง Node 
            add_node = Node(data)
            add_node.next = None
            self.head = add_node
            self.tail =  add_node
    def Add_Last_Data(self,data):   #สร้าง Method เพื่อเพิ่ม Node จากข้างหลัง
        if self.head != None:   #สร้างเงื่อนไขหากเคยสร้าง Node มาก่อนแล้ว
            add_node = Node(data)
            add_node.next = None
            self.tail = add_node
        else:       #เพิ่มเงื่อนไขกรณีที่ยังไม่เคยสร้าง Node 
            add_node = Node(data)
            self.head = add_node
            self.tail = add_node
            add_node.next = None
    def Front_Delete(self):     #สร้าง Method เพื่อลบ Node จากด้านหน้า
        if self.head == None:   #สร้างเงื่อนไขหากไม่มี Node อยู่ใน LinkedList
            print("ไม่สามารถลบข้อมูลได้เพระา Linked List ว่าง")
        else:       #เงื่อนไขหากมี Node อยู่ใน LinkedList
            self.head = self.head.next          
    def Last_Delete(self):      #สร้าง Method เพื่อลบ Node จากข้างหลัง
        if self.head == None:   #สร้างเงื่อนไขหากไม่มี Node อยู่ใน LinkedList
             print("ไม่สามารถลบข้อมูลได้เพระา Linked List ว่าง")
        else:       #เงื่อนไขหากมี Node อยู่ใน LinkedList
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
    def Manual_Delete(self,data):   #สร้าง Method เพื่อลบ Node แบบกำหนดเอง
        if self.head == None:   #สร้างเงื่อนไขหากไม่มี Node อยู่ใน LinkedList
            print("ไม่สามารถลบข้อมูลได้เพระา Linked List ว่าง")
        else:   #เงื่อนไขหากมี Node อยู่ใน LinkedList
            temp = self.head
            previous = self.head
            if temp.info == data:   #สร้างเงื่อนไขเพื่อตรวจสอบ Node ว่าตรงกับข้อมูลที่ต้องการลบหรือไม่
                self.head = self.head.next  
                return
            elif self.tail.info == data:    #เพิ่มเงื่อนไขหากข้อมูลที่ต้องการจะลบนั้นตรงกับ Node ที่ Pointer Tail ชี้อยู่พอดี
                self.Last_Delete()
                return
            while temp.info != data:    #เพิ่มลูปเพื่อให้ Pointer ไล่หาข้อมูลที่ต้องการจะลบ
                if temp == self.tail and temp.info != data: #เพิ่มเงื่อนไขในกรณีที่หาข้อมูลไม่พบ
                    print("ไม่มีข้อมูลที่ต้องการลบใน Linked List")
                previous = temp
                temp = temp.next
            previous.next = temp.next
    def display(self):      #สร้าง Method เพื่อแสดงผลข้อมูลออกทางหน้าจอ
        if self.head == None:   #สร้างเงื่อนไขหากไม่มี Node อยู่ใน LinkedList
            print("ไม่สามารถแสดงข้อมูลได้เพระา Linked List ว่าง")
        else:   #เงื่อนไขหากมี Node อยู่ใน LinkedList
            print("Head =",self.head.info,"\tTail =",self.tail.info)
            temp = self.head
            while temp != None:     #เพิ่มลูปเพื่อแสดงข้อมูลใน Node
                print("ข้อมูลที่จัดเก็บ =",temp.info) 
                temp = temp.next


ListClass = LinkedList()    
print("โปรดระบุทางเลือกในการดำเนินการกับ Singly Linked List\n"
            f"\t1. เพิ่มข้อมูลที่จุดเริ่มต้น Singly Linked List\n"
            f"\t2. เพิ่มข้อมูลที่จุดสิ้นสุด Singly Linked List\n"
            f"\t3. ลบข้อมูลที่จุดเริ่มต้น Singly Linked List\n"
            f"\t4. ลบข้อมูลที่จุดสิ้นสุด Singly Linked List\n"
            f"\t5. ลบข้อมูลที่ระบุจาก Singly Linked List\n"
            f"\t6. แสดงข้อมูลที่จัดเก็บทั้งหมดใน Singly Linked List\n")
choice = int(input("ทางเลือกในการดำเนินการ : "))   #รับค่าทางคีย์บอร์ดจากผู้ใช้
while choice <= 6 and choice >= 1:  #สร้างลูปเพื่อวนซ้ำรับค่าทางคีย์บอร์ดจากผู้ใช้

    if choice == 1: #สร้างเงื่อนไขหากผู้ใช้เลือกตัวเลือกที่ 1
        data = int(input("ข้อมูลที่ต้องการเพิ่มที่จุดเริ่มต้น Singly Linked List = "))
        ListClass.Add_Front_Data(data)
    elif choice == 2:   #สร้างเงื่อนไขหากผู้ใช้เลือกตัวเลือกที่ 2
        data = int(input("ข้อมูลที่ต้องการเพิ่มที่จุดสิ้นสุด Singly Linked List = "))
        ListClass.Add_Last_Data(data)

    elif choice == 3:   #สร้างเงื่อนไขหากผู้ใช้เลือกตัวเลือกที่ 3
        ListClass.Front_Delete()

    elif choice == 4:   #สร้างเงื่อนไขหากผู้ใช้เลือกตัวเลือกที่ 4
        ListClass.Last_Delete()

    elif choice == 5:   #สร้างเงื่อนไขหากผู้ใช้เลือกตัวเลือกที่ 5
        data = int(input("ข้อมูลที่ต้องการลบจาก Singly Linked List = "))
        ListClass.Manual_Delete(data)

    elif choice == 6:   #สร้างเงื่อนไขหากผู้ใช้เลือกตัวเลือกที่ 6
        ListClass.display()



    print("โปรดระบุทางเลือกในการดำเนินการกับ Singly Linked List\n"
            f"\t1. เพิ่มข้อมูลที่จุดเริ่มต้น Singly Linked List\n"
            f"\t2. เพิ่มข้อมูลที่จุดสิ้นสุด Singly Linked List\n"
            f"\t3. ลบข้อมูลที่จุดเริ่มต้น Singly Linked List\n"
            f"\t4. ลบข้อมูลที่จุดสิ้นสุด Singly Linked List\n"
            f"\t5. ลบข้อมูลที่ระบุจาก Singly Linked List\n"
            f"\t6. แสดงข้อมูลที่จัดเก็บทั้งหมดใน Singly Linked List\n")
    choice = int(input("ทางเลือกในการดำเนินการ : "))
'''
    
    
        
''' Treeeeeeeeeeeeeeee
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def Pre_Order(tree):
    if tree.data == None:
        return
    print(tree.data)
    Pre_Order(tree.left)
    Pre_Order(tree.right)

def In_Order(tree):
    if tree.data == None:
        return
    In_Order(tree.left)
    print(tree.data)
    In_Order(tree.right)

def Post_Order(tree):
    if tree.data == None:
        return
    Post_Order(tree.left)
    Post_Order(tree.right)
    print(tree.data)

def Insert(tree, data):
    i = input("L/R : ")
    if i == "L":
        if tree.left is None:
            tree.left = Node()
            tree.left.data = data
            return
        else:
            Insert(tree.left, data)
    if i == "R":
        if tree.right is None:
            tree.right = Node()
            tree.right.data = data
            return
        else:
            Insert(tree.right, data)

Tree = Node()
Tree.data = int(input("Root : "))
while True:
    op = int(input("1/2/3/4 : "))
    if op == 1:
        Pre_Order(Tree)
    elif op == 2:
        In_Order(Tree)
    elif op == 3:
        Post_Order(Tree)
    elif op == 4:
        Insert(Tree, int(input("Data : ")))
    else:
        break
'''
