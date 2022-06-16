class Hash_table:   #ประกาศ Class ชื่อ Hash_Table
    def __init__(self, hash_size):
        self.size = [None]*hash_size    #สร้าง List เพื่อเก็บข้อมูลใน List
        self.collision = 0  # สร้างตัวแปรเพื่อเก็บค่าจำนวนครั้งที่
 
    def data_append(self, key, data):
        if self.size[key] == None:      #สร้างเงื่อนไขเพื่อตรวจสอบว่ามีข้อมูลอยู่ในช่องนั้นหรือไม่
            self.size[key] = data   #แทนที่ค่า None ด้วยข้อมูลในใตัวแปร data
        else:
            print("จัดเก็บข้อมูลในตารางไม่ได้เพราะตำแหน่งดังกล่าวในตารางแฮชจัดเก็บข้อมูล",self.size[key])
            self.collision += 1     

hash_size = int(input("โปรดป้อนขนาดตารางแฮช : "))
HashTable = Hash_table(hash_size)   #สร้าง Object ชื่อ HashTable

key = int(input("โปรดป้อนค่าคีย์ (key) ที่มีค่าตั้งแต่ 0 ขึ้นไป : "))
data = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตารางแฮช : ")
while True:
    if key < 0:
        break
    HashTable.data_append(key % hash_size, data)
    key = int(input("โปรดป้อนค่าคีย์ (key) ที่มีค่าตั้งแต่ 0 ขึ้นไป : "))
    data = input("โปรดป้อนข้อมูล (data) ที่เป็นข้อความเพื่อจัดเก็บข้อมูลในตารางแฮช : ")

for x in range(hash_size):
    if HashTable.size[x] == None:       #ตรวจสอบข้อมูลในช่องที่ x ว่ามีค่าเป็น None หรือไม่
        print("index",x,", ไม่มีข้อมูลจัดเก็บ")
    else:
        print("index",x,", ข้อมูลคือ", HashTable.size[x])
print("จำนวนครั้งที่เกิด Collision =", HashTable.collision)