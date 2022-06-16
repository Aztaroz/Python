class Node: #สร้าง Class node
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def in_ordered(self, object): # สร้างฟังก์ชั่น in-ordered
        if object == None:      # สร้างเงื่อนไขเพื่อตรวจสอบว่า node ถัดไปว่างหรือไม่
            return
        self.in_ordered(object.left)
        print(object.data)
        self.in_ordered(object.right)

    def post_ordered(self, object): # สร้างฟังก์ชั่น post-ordered
        
        if object:
            self.post_ordered(object.left)
            self.post_ordered(object.right)
            if object.data.startswith("a"): # สร้างเงื่อนไขสำหรับคัดกรองตัวอักษรขึ้นต้น
                print(object.data)
            if object.data.startswith("e"):
                print(object.data)
            if object.data.startswith("i"):
                print(object.data)
            if object.data.startswith("o"):
                print(object.data)
            if object.data.startswith("u"):
                print(object.data)

    def insert(self,data): # สร้างฟังก์ชั่น insert สำหรับใส่ข้อมูล
        if data != " ":     # สร้างฟังก์ชั่นเพื่อตรวจสอบหากผู้ใช้ใส่ค่าว่าง
            self.data = data
        else:
            return
        print("โปรดป้อนข้อความเพื่อจัดเก็บที่โหนด Left Child ของ",self.data,end="")
        data = input("(ถ้าไม่มีให้ป้อนค่าช่องว่าง 1 ช่อง) : ")
        if data != " ": # สร้างฟังก์ชั่นเพื่อตรวจสอบหากผู้ใช้ใส่ค่าว่าง
            self.left = Node()
            self.left.insert(data)

        print("โปรดป้อนข้อความเพื่อจัดเก็บที่โหนด Right Child ของ",self.data,end="")
        data = input("(ถ้าไม่มีให้ป้อนค่าช่องว่าง 1 ช่อง) : ")
        if data != " ": # สร้างฟังก์ชั่นเพื่อตรวจสอบหากผู้ใช้ใส่ค่าว่าง
            self.right = Node()
            self.right.insert(data)
    

TreeObject = Node() # สร้าง Object ชื่อ TreeObject
data = input("โปรดป้อนข้อความเพื่อจัดเก็บที่ Root node : ") # รับค่าสำหรับ Root
TreeObject.insert(data) #เรียกใช้ Method Insert
print("ผลลัพธ์จาการท่องไปในต้นไม้ทวิภาคด้วยขั้นตอนวิธีแบบ In-order :")
TreeObject.in_ordered(TreeObject) #เรียกใช้ Method in-ordered
print("ผลลัพธ์จากการท่องไปในต้นไม้ทวิภาคด้วยขั้นตอนวิธีแบบ Post-order โดยแสดงข้อความที่จัดเก็บในแต่ละโหนดที่ขึ้นต้นด้วยตัวอักษร a หรือ e หรือ i หรือ o หรือ u :")
TreeObject.post_ordered(TreeObject) #เรียกใช้ Method post-ordered