import cv2

img = cv2.imread('./img/t4.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold_img = cv2.threshold(gray_img, 160, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("threshold_img", threshold_img)

# 处理亮处
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
dilate_img = cv2.dilate(threshold_img, dilate_kernel)
cv2.imshow("dilate_img", dilate_img)


key = cv2.waitKey(0)
if key == 27:
    print(key)
    cv2.destroyAllWindows()