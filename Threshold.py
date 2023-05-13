import cv2
import matplotlib.pyplot as plt

img=cv2.imread('cat.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
#如下图中，像素点大于127的地方为255，显示白，亮； 像素点小于127的地方为0，显黑

ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
#如下图cv2.THRESH_BINARY_INV是 THRESH_BINARY的颜色反转

ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
#如下图中，像素点大于127的地方为127， 像素点小于127的地方不变

ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
#如下图中，像素点大于127的地方为不变， 像素点小于127的地方为0

ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)
#如下图中，像素点大于127的地方为0， 像素点小于127的地方为不变

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
