import cv2
img = cv2.imread('eagle.jpg') #读取一张图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#进行灰度转换
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)#进行2值处理

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#第一个值binary就是二值处理的结果,第二个值contours是轮廓点的信息,
#需要注意的是,旧版本的opencv返回上面三个值,新版本的opencv已经不再返回binary的值了
#contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#绘制轮廓
#传入绘制图像，轮廓，轮廓索引，颜色模式，线条厚度
# 注意需要copy,要不原图会变。。。
draw_img = img.copy()   #图片拷贝
res = cv2.drawContours(draw_img, contours, -1, (0, 0, 255), 2)
#第三个参数告诉它要画第几个轮廓,其中-1代表着画出所有的轮廓
#(0,0,255)代表用什么颜色去画轮廓,(b,g,r)颜色通道,这里表示用红色去画
#最后一个参数是线条的宽度

cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
