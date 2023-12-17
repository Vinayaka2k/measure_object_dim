import cv2
import numpy as np

# distances from the camera
distances = [12, 24, 36]

image_dimensions = []
image_paths = ['12cm.jpg', '24cm.jpg', '36cm.jpg']

for index, distance in enumerate(distances):

    img = cv2.imread(image_paths[index])
    
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image', 600, 800)
    cv2.imshow('Image', img)
    cv2.waitKey(0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image', 600, 800)
    cv2.imshow('Image', gray)
    cv2.waitKey(0)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_with_contours = img.copy()
    cv2.drawContours(img_with_contours, contours, -1, (0, 255, 0), 3)
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image', 600, 800)
    cv2.imshow('Image', img_with_contours)
    cv2.waitKey(0)

    contour = contours[0]

    x, y, w, h = cv2.boundingRect(contour)
    image_dimensions.append({'width': w, 'height': h})

scale_factors = [{'width': d / dim['width'], 'height': d / dim['height']} for d, dim in zip(distances, image_dimensions)]

avg_scale_factors = {
    'width': sum(sf['width'] for sf in scale_factors) / len(scale_factors),
    'height': sum(sf['height'] for sf in scale_factors) / len(scale_factors)
}

actual_dimensions = {
    'width': avg_scale_factors['width'] * image_dimensions[0]['width'],
    'height': avg_scale_factors['height'] * image_dimensions[0]['height']
}

print("Actual Dimensions:", actual_dimensions)

cv2.destroyAllWindows()