import cv2

def findTemplate(img, temp, method):
    res = cv2.matchTemplate(img, temp, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0]+temp.shape[1], top_left[1]+temp.shape[0])
    return top_left, bottom_right

if __name__ == '__main__':
    img = cv2.imread('contact_info.png')
    temp = cv2.imread('template.png')
    top_left, bottom_right = findTemplate(img, temp, cv2.TM_SQDIFF)
    cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 5)
    cv2.namedWindow('object_detection', cv2.WINDOW_NORMAL)
    cv2.imshow('object_detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()