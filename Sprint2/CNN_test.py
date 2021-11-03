# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:57:30 2021

@author: xy
"""


import cv2
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

image = cv2.imread('example.png')

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

image_small_size = cv2.resize(image, (110, 66))
image_bigger = cv2.resize(image, (640, 384))


plt.imshow(cv2.cvtColor(image_small_size, cv2.COLOR_BGR2RGB))
# as opencv loads in BGR format by default, we want to show it in RGB.
plt.show()

plt.imshow(cv2.cvtColor(image_bigger, cv2.COLOR_BGR2RGB))
# as opencv loads in BGR format by default, we want to show it in RGB.
plt.show()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

haar_cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces_rects = haar_cascade_face.detectMultiScale(image, scaleFactor = 1.2, minNeighbors = 5);

# Let us print the no. of faces found
print('Faces found: ', len(faces_rects))

for (x,y,w,h) in faces_rects:
     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# as opencv loads in BGR format by default, we want to show it in RGB.
plt.show()
