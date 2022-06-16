import math

class Queue:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
class Vertex:
    def __init__(self,data):
        self.id = data
        self.distance = math.inf
        self.color = 'white'
        self.pled = None
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight = 0):
        self.connectedTo[nbr] = weight
    
    def setColor(self,color):
        self.color = color

    def setDistance(self,d):
        self.distance = d
    
    def setPred(self,p):
        self.pred = p

    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getPred(self):
        return self.pred
    
    def getDistance(self):
        return self.distance

    def getColor(self):
        return self.color
    
class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t):
        if f not in self.vertices:
            nv = self.addVertex(t)
        if t not in self.vertices:
            nv = self.addVertex(f)
        self.vertices[f].addNeighbor(self.vertices[t])

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())
    
    #! BFS
    def bfs(self,start):
        s = self.getVertex(start)
        s.setDistance(0)
        s.setPred(None)
        q = Queue()
        q.enqueue(s)
        while not(q.isEmpty()):
            currentVertex = q.dequeue()
            for nbr in currentVertex.getConnections():
                if(nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVertex.getDistance()+1)
                    nbr.setPred(currentVertex)
                    q.enqueue(nbr)
                    print("ระยะทางที่สั้นที่สุดจากจุดเริ่มต้นในการท่องไปในกราฟไปยังจุด",nbr.getId(),'=',nbr.getDistance())
            currentVertex.setColor('black')

g = Graph() #สร้าง Class Graph
loop = int(input("โปรดระบุจำนวนจุดในกราฟ : "))
for i in range(loop):       
    name = input("โปรดระบุชื่อ Vertex : ")
    g.addVertex(name)   # ทำการเพิ่มจุดยอดให้กับกราฟ

f = None
t = None

print("โปรดระบุชื่อ source และ destination ของเส้นเชื่อม")
f = input("source = ")
t = input("destination = ")
g.addEdge(f,t)      # เพิ่มเส้นเชื่อมจากจุด f ไปยังจุด t ในกราฟ g

while True:
    if f and t == "-":  # จะหยุดทำงานของโปรแกรมเมื่อทำการระบุ source และ destination เป็น -
        break
    else:
        print("โปรดระบุชื่อ source และ destination ของเส้นเชื่อม")
        f = input("ชื่อจุดที่เป็น source = ")
        t = input("ชื่อจุดที่เป็น destination = ")
        g.addEdge(f,t)      # ทำการเพิ่มเส้นเชื่อมจากจุด f ไปยังจุด t ในกราฟ g

print("โปรดระบุชื่อจุดที่เริ่มต้นในการท่องไปในกราฟด้วยขั้นตอนวิธีแบบ Breadth-first Search")
start = input("ชื่อจุดที่เป็นจุดเริ่มต้นในการท่องไปในกราฟ = ")
g.bfs(start)        # ทำการค้นหาเส้นทางที่สั้นที่สุดจากจุดเริ่มต้นในการท่องไปในกราฟด้วยวิธีแบบ Breadth-first Search

    
    




