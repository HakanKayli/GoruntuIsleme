
import cv2
from matplotlib import pyplot as plt
from numpy import zeros, shape


foto = cv2.imread("kaptanamerika.jpeg",0)

Hist = zeros(256)
[w,h] = shape(foto)

for i in range (0,w):
    for j in range (0,h):
        a = foto[i,j]
        Hist[a] = Hist[a] + 1

plt.plot(Hist)
#plt.stem(Hist)
plt.show()

cv2.imshow("alaycı kus", foto)
cv2.waitKey()


#Hazır Fonksiyon
'''foto = cv2.imread("kus.jpg",0)
hist = cv2.calcHist([foto], [0],None,[256], [0,256])
#plt.figure(1)
plt.plot(hist)
plt.show()

cv2.imshow("kus",foto)
cv2.waitKey()'''

