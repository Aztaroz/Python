import pandas as pd
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('black-cat-kitchen-rug-getty.jpg')

output = cv2.resize(img,(1000,1000))

frameGRAY = cv2.cvtColor(output,cv2.COLOR_RGB2GRAY)
plt.imshow(frameGRAY)
plt.title("frameGRAY")
plt.show()
print("frameGRAY:",frameGRAY.shape)
print(frameGRAY)