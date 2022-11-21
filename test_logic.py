from pymongo import MongoClient

print("test script")

myclient = MongoClient('mongodb://localhost:27017')

print(myclient.list_database_names())

mydb = myclient['hellofrommongo']
mycol = myclient['module4']

myquery = {'items':'journal'}
data = mycol.find(myquery)
print(data)
