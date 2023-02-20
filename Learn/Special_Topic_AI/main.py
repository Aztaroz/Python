import numpy as np

a = np.array([2,3,4])
b = np.array([(1.5,2,3),(2,5,6)])
c = np.arange(15).reshape(3,5)
d = np.zeros((3,4))
e = np.ones((2,3,4), dtype=np.int16)

# print(b)
print(b[0][1])