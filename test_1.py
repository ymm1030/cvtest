import cv2
from matplotlib import pyplot as plt

img = cv2.imread('xiaoxiao.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img)
# plt.xticks([]), plt.yticks([])
# plt.show()