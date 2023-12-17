import cv2
import numpy as np

# Example distances from the camera
distances = [0.5, 1.0, 1.5]

# Placeholder for image dimensions obtained from OpenCV
image_dimensions = []
image_paths = ['12cm.jpg', '24cm.jpg', '36cm.jpg']

# Step 1: Click on the Object at Different Distances
for index, distance in enumerate(distances):
    # Capture image from the camera (replace this with your camera capture code)
    # For simplicity, we are using a placeholder image
    img = cv2.imread(image_paths[index])  # Replace with your image path
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)

    # Step 2: RGB to Gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 3: Thresholding
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Step 4: Find Contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assume there is only one contour (replace with logic to handle multiple contours)
    contour = contours[0]

    # Step 5: Obtain Image Dimensions
    x, y, w, h = cv2.boundingRect(contour)
    image_dimensions.append({'width': w, 'height': h})

# Step 6: Calculate Image Scale Factors
scale_factors = [{'width': d / dim['width'], 'height': d / dim['height']} for d, dim in zip(distances, image_dimensions)]

# Step 7: Average Scale Factors
avg_scale_factors = {
    'width': sum(sf['width'] for sf in scale_factors) / len(scale_factors),
    'height': sum(sf['height'] for sf in scale_factors) / len(scale_factors)
}

# Step 8: Find Real-World Dimensions
actual_dimensions = {
    'width': avg_scale_factors['width'] * image_dimensions[0]['width'],
    'height': avg_scale_factors['height'] * image_dimensions[0]['height']
}

print("Actual Dimensions:", actual_dimensions)

cv2.destroyAllWindows()