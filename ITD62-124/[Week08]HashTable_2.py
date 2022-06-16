# With Class
class Hash_table:   #ประกาศ Class ชื่อ Hash_Table
    def __init__(self, hash_size):
        self.size = [None]*hash_size    #สร้าง List เพื่อเก็บข้อมูลใน List
        self.collision = 0  # สร้างตัวแปรเพื่อเก็บค่าจำนวนครั้งที่
 
    def data_append(self, hash, data, key, hash_size):
        self.collision = 0          #สร้างตัวแปรเพื่อเก็บค่าจำนวนครั้งที่ชนกัน
        if self.size[hash] == None:      #สร้างเงื่อนไขเพื่อตรวจสอบว่ามีข้อมูลอยู่ในช่องนั้นหรือไม่
            self.size[hash] = data   #แทนที่ค่า None ด้วยข้อมูลในตัวแปร data
            print("Address :",hash)
        else:
            while True:
                self.collision += 1     
                sum = (key + self.collision) % hash_size  #คำนวน Hash Table Function 2 แล้วเก็บไว้ในตัวแปร sum
                if self.size[sum] == None:
                    self.size[sum] = data   #แทนที่ค่า None ด้วยข้อมูลในตัวแปร data
                    print("Address :",sum)
                    break
                else:
                    self.collision +=1

hash_size = int(input("โปรดป้อนขนาดตารางแฮช : "))
HashTable = Hash_table(hash_size)   #สร้าง Object ชื่อ HashTable

key = int(input("โปรดป้อนค่าคีย์ (key) ที่มีค่ามากกว่าหรือเท่ากับ 0: "))
data = input("โปรดป้อนข้อมูลชื่อสินค้าเพื่อจัดเก็บในตารางแฮช: ")

while True:
    if key < 0:
        break
    HashTable.data_append(key % hash_size, data, key, hash_size)    #เรียกใช้ Method ชื่อ data append โดยส่งค่า hash (key % hash_size) ไป
    key = int(input("โปรดป้อนค่าคีย์ (key) ที่มีค่ามากกว่าหรือเท่ากับ 0: "))
    data = input("โปรดป้อนข้อมูลชื่อสินค้าเพื่อจัดเก็บในตารางแฮช: ")

for x in range(hash_size):
    if HashTable.size[x] == None:       #ตรวจสอบข้อมูลในช่องที่ x ว่ามีค่าเป็น None หรือไม่
        print("Address =",x,", ไม่มีข้อมูลจัดเก็บ")
    else:
        print("Address =",x,", ข้อมูลที่จัดเก็บคือ", HashTable.size[x])



# Without Class
'''
def insert_data(hash, list, data):
    collision = 0
    if list[hash] == None:
        list[hash] = data
        print("Address :", hash)
    else:
        collision += 1
        hash_fn2 = (key + collision) % hash_size
        list[hash_fn2] = data
        print("Address :", hash_fn2)

hash_size = int(input("Insert Hash Size : "))
list = [None]*hash_size

while True:
    key = int(input("Insert Key (>=0) : "))
    data = input("Insert Data : ")
    if key < 0:
        break
    insert_data(key % hash_size, list, data)

for x in range(hash_size):
    if list[x] == None:
        print("Address =",x,"No Data")
    else:
        print("Address =",x,"Data is",list[x])
'''