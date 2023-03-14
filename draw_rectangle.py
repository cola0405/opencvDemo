import cv2

img = cv2.imread('./img/t4.png')

start_y = 10
end_y = 50

start_x = 50
end_x = 100


rect_img = cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (255, 0, 0), thickness=1)
cv2.imshow("img", rect_img)

key = cv2.waitKey(0)
if key == 27:
    print(key)
    cv2.destroyAllWindows()