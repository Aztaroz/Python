class node:     # สร้าง Class Node
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
    
    def post_ordered(self, object): # สร้างฟังก์ชั่น post-ordered
        if object:
            self.post_ordered(object.left)
            self.post_ordered(object.right)
            print(object.data,end=" ")

    def find_largest_node (self): # สร้างเมธอดเพื่อหาค่าที่มากที่สุด
        if self.right == None:
            return self.data    # Return ค่าออกไปหากไม่มีโหนดด้านขวาแล้ว
        return self.right.find_largest_node()   # ใช้ Recursive Function

    def insert (self, data):    # สร้างเมธอดเพื่อใส่ข้อมูล
        if self.data == None:
            self.data = data
        elif data < self.data:
            if self.left == None:
                self.left = node()
                self.left.data = data
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right == None:
                self.right = node()
                self.right.data = data
            else:
                self.right.insert(data)


TREE_CLASS = node() #สร้าง Object ชื่อ TREE_CLASS

print("โปรดป้อนจำนวนเต็มเพื่อจัดเก็บใน Binary search tree ถ้าไม่ต้องการเพิ่มข้อมูลอีกให้ป้อนค่าตัวเลข 12345")
while True:
    data = int(input("ข้อมูล = "))
    if data == 12345:   
        break       # ให้ Break Loop เมื่อค่าของตัวแปร data = 12345
    else:
        TREE_CLASS.insert(data) # เรียกใช้เมธอด insert โดยอ้างอิงจาก object TREE_CLASS

print("ผลลัพธ์จากการท่องไปใน Binary search tree ด้วยขั้นตอนวิธีแบบ Post-order")
TREE_CLASS.post_ordered(TREE_CLASS) #เรียกใช้เมธอด post_ordered
print("\nจำนวนเต็มมากที่สุดจัดเก็บใน Binary search tree คือ",TREE_CLASS.find_largest_node())    #เรียกใช้เมธอด find_largest_node


