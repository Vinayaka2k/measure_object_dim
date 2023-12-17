import cv2
img = cv2.imread("./cup_image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray, 127, 155, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
print(contours)
cv2.drawContours(img, contours, -1, (0,0,255), 2)
cv2.imwrite('res.jpeg', img)