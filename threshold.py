import cv2

img = cv2.imread('./img/t4.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold_img = cv2.threshold(gray_img, 160, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("threshold_img", threshold_img)

key = cv2.waitKey(0)
if key == 27:
    print(key)
    cv2.destroyAllWindows()