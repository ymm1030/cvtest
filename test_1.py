import cv2
from matplotlib import pyplot as plt

img = cv2.imread('xiaoxiao.jpg')
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
plt.imshow(img2)
plt.xticks([]), plt.yticks([])
plt.show()