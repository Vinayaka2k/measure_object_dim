import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./cup_image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# plt.imshow(gray, cmap="gray")
# plt.title('Grayscale Image')
# plt.show()

ret,thresh = cv2.threshold(gray, 127, 255, 0)
# plt.imshow(thresh, cmap="gray")
# plt.title('Thresholded Image')
# plt.show()

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0,255,0), 2)

plt.imshow(contour_img)
plt.title('Image with Contours')
plt.show()
# cv2.imwrite('res.jpeg', img)