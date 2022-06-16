'''
import numpy as np
matrix = np.array([[0,1,2],[3,5,9],[5,7,9]])
mat = np.array([[0,0,8], [7,5,3], [4,5,6], [9,4,5], [1,2,3]])
print(mat[1,2])
'''


avg = 0
age = [10,12,15,16,18]
avg = avgAge
print("average of age is {}".format())

'''
person_dict = {
    "fname": "K",
    "lname": "B",
    "age": 0.5,
    "body_temp": "20",
    "location": "A",
    "risk": False,
    "covid": False
}
print(person_dict.values())
#print("Name {:.2f}".format(person_dict.get("age")))
'''

'''
def displayAge(*age):
    #i = 1
    for i in age:
        print("Age #{} : {}\n".format(i,age[i]))
        #i += 1
'''

'''
age = [10,15,20]
person = 3
for i in range(person):
    print(age[i])
'''

'''
def avgAge(age,n):
    avg = 0
    sumAge = 0
    for x in range(n):
        sumAge = sumAge + age[x]
    avg = sumAge/n
    return avg

age = [10,20]
print(avgAge(age,2))
'''

'''
age = [10,20]
n = 2
i = 1
for x in range(n):
    print("Age#{} : {}\n".format(i,age[x]))
    i+=1
'''