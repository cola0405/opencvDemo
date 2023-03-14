import cv2

img = cv2.imread('./img/t4.png')

start_y = 10
end_y = 50

start_x = 50
end_x = 100
img = img[start_y:end_y, start_x:end_x]
img = cv2.imshow('img', img)


key = cv2.waitKey(0)
if key == 27:
    print(key)
    cv2.destroyAllWindows()