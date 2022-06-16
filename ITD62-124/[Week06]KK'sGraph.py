class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
        # destination, w คือ  weight
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w]) #เมื่อมีการเพิ่มเส้นเชื่อมจะมีการเพิ่มข้อมูลใน List
    

    def find_set(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]


    def union(self, parent, rank, x, y):
        x = self.find_set(parent, x)
        y = self.find_set(parent, y)
        if rank[x] < rank[y]:
            parent[x] = y 
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] = rank[x] + 1

#! Kruskal
    def kruskal(self):
        A = []
        self.graph = sorted(self.graph, key= lambda item: item[2])
        print()
        parent = []
        rank =[]
        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)
        i = 0
        e = 0
        sumedge = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_set(parent,u)
            y = self.find_set(parent, v)
            if x != y:
                e = e + 1
                A.append([u, v, w])
                self.union(parent, rank, x, y)
            print("เส้นเชื่อมระหว่างจุด",u,"กับจุด",v,"มีค่าน้ำหนัก =",w)
            sumedge += w        #หาผลรวมของน้ำหนักทั้งหมด
        print("Weight รวมของ Minimum spanning tree คือ",sumedge)
        


n = int(input("โปรดระบุค่าตัวแปร n (จำนวนจุดในกราฟแบบไม่มีทิศทาง (Undirected graph)) : "))
g = Graph(n)        #สร้าง Object 
edge = int(input("โปรดระบุจำนวนเส้นเชื่อม (Edge) ในกราฟแบบไม่มีทิศทาง : "))
print("โปรดระบุชื่อจุดที่เป็น Source ชื่อจุดที่เป็น Destination และค่าน้ำหนัก (Weight) ของเส้นเชื่อมในกราฟ : ")
for x in range(edge):       #วนลูปเพื่อรับค่า Source, Destination, Weight
    print("#",x+1,"time")
    source = int(input("Source = "))
    destination = int(input("Destination : "))
    weight = int(input("Weight : "))
    g.addEdge(source, destination, weight)      #เรียกใช้ Method addEdge
g.kruskal()     #เรียกใช้ Method kruskal
