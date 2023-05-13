import cv2 as cv

# 1、读取图片，转灰度图
img = cv.imread('improve_car.jpg')
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# cv.imshow('gray', gray)

# 2、提取轮廓（Sobel算子提取y方向）
y = cv.Sobel(gray, cv.CV_16S, 1,     0)
# 注：对x/y微分和得到x/y方向图像相反  要得到x/y方向边缘，就要求y/x方向的微分。
absY = cv.convertScaleAbs(y)
# cv.imshow('Y', absY)

# 3、自适应二值化
ret, binary = cv.threshold(absY, 0, 255, cv.THRESH_OTSU)
# cv.imshow('binary', binary)

# 4、闭运算处理，把图像闭合、揉团，使图像区域化，便于找到车牌区域，进而得到轮廓
kernel = cv.getStructuringElement(cv.MORPH_RECT, (17,5))
print('kernel= \n', kernel)
close = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
# cv.imshow('close', close)

kernel_x = cv.getStructuringElement(cv.MORPH_RECT, (25, 7))
kernel_y = cv.getStructuringElement(cv.MORPH_RECT, (1, 11))

# 5-1、水平方向腐蚀/膨胀
erode = cv.morphologyEx(close, cv.MORPH_ERODE, kernel_x)
# cv.imshow('erode_x', erode)
dilate = cv.morphologyEx(erode, cv.MORPH_DILATE, kernel_x)
# cv.imshow('dilate_x', dilate)

# 5-2、竖直方向腐蚀/膨胀
erode_y = cv.morphologyEx(dilate, cv.MORPH_ERODE, kernel_y)
# cv.imshow('erode_y', erode)
dilate_y = cv.morphologyEx(erode, cv.MORPH_DILATE, kernel_y)
# cv.imshow('dilate_y', dilate)



# 6-1、得到轮廓
contours, hierarchy = cv.findContours(dilate_y, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
img_copy = img.copy()
# 6-2、画出轮廓
cv.drawContours(img_copy, contours, -1, (255,0,255), 2)
# cv.imshow('Contours', img_copy)

# 6、获取外轮廓
# img_copy = img.copy()
# 6-1、得到轮廓
contours, hierarchy = cv.findContours(dilate_y, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# 6-2、画出轮廓并显示
cv.drawContours(img_copy, contours, -1, (255,0,255), 2)
cv.imshow('Contours', img_copy)

# 7、遍历所有轮廓，找到车牌轮廓
for contour in contours:
    # 7-1、得到矩形区域：左顶点坐标、宽和高
    rect = cv.boundingRect(contour)
    # 7-2、判断宽高比例是否符合车牌标准，截取符合图片
    if rect[2] > rect[3] * 3 and rect[2] < rect[3] * 5:
        # 截取车牌并显示
        img = img[rect[1]:(rect[1] + rect[3]), rect[0]:(rect[0] + rect[2])]
#        cv.nameWindows('license plate',cv.WINDOW_NORMAL)
        cv.imshow('license plate', img)

cv.waitKey(0)  # 显示5秒
# 销毁所有的窗口
cv.destroyAllWindows()