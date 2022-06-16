
class Node():   #สร้าง Class Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree():   #สร้าง Class AVL_Tree
    def getHeight(self, root):  #สร้างฟังก์ชั่น getHeight
        if not root: # ถ้า root เป็น None จะคืนค่า 0
            return 0    
        return root.height
    
    def getBalance(self, root): # สร้างฟังก์ชั่น getBalance
        if not root: # ถ้า root เป็น None จะคืนค่า 0
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right) # คืนค่า root.left - root.right
    
    def leftRotate(self, z):    #สร้างฟังก์ชั่น leftRotate
        y = z.right # กำหนด y เป็น z.right
        x = y.left  # กำหนด x เป็น y.left
        y.left = z
        z.right = x
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        x = y.right
        y.right = z
        z.left = x
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def pre_ordered(self, object): # สร้างฟังก์ชั่น post-ordered
        if object:
            print(object.data,end=" ")
            self.pre_ordered(object.left)
            self.pre_ordered(object.right)
            

    def insert(self, root, key):
        if not root:    # ถ้า root เป็น None จะทำการสร้าง Node ใหม่
            return Node(key)    # สร้าง Node ใหม่
        elif key < root.data:   # ถ้า key น้อยกว่า root.data จะทำการสร้าง Node ใหม่
            root.left = self.insert(root.left, key)
        else:   # ถ้า key มากกว่า root.data จะทำการสร้าง Node ใหม่
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))    
        balance = self.getBalance(root) 
        if balance > 1 and key < root.left.data:    # ถ้า balance มากกว่า 1 และ key น้อยกว่า root.left.data จะทำการสร้าง Node ใหม่
            return self.rightRotate(root)
        if balance > 1 and key > root.left.data:    # ถ้า balance มากกว่า 1 และ key มากกว่า root.left.data จะทำการสร้าง Node ใหม่
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.data:  # ถ้า balance น้อยกว่า -1 และ key น้อยกว่า root.right.data จะทำการสร้าง Node ใหม่
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        if balance < -1 and key > root.right.data:  # ถ้า balance น้อยกว่า -1 และ key มากกว่า root.right.data จะทำการสร้าง Node ใหม่
            return self.leftRotate(root)
        
        return root

avl = AVL_Tree()    # สร้าง Object ของ Class AVL_Tree
root = None   # สร้าง root เป็น None
while True:
    data = int(input("โปรดป้อนจำนวนเต็มเพื่อสร้าง AVL Tree: "))
    if data == 9999:
        break
    root = avl.insert(root,data)     # สร้าง root เป็น data
print("ผลลัพธ์ที่ได้จากการท่องไปใน AVL tree ด้วยขั้นตอนวิธีแบบ Pre-order")
avl.pre_ordered(root)   # เรียกใช้ฟังก์ชั่น pre-ordered
