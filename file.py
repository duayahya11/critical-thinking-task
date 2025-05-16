import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path)
    return image

def calculate_brightness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.mean(gray)

def is_colorful(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    saturation = hsv[:, :, 1]
    high_sat = np.sum(saturation > 80)
    return high_sat > (0.2 * saturation.size)

def assign_belt(image):
    brightness = calculate_brightness(image)
    
    if brightness > 170:
        return "B", "Transparent"
    elif is_colorful(image):
        return "C", "Colorful"
    else:
        return "A", "Black"

if __name__ == "__main__":
    test_image_path = "dataset/colorful/fourth.jpg" 
    img = load_image(test_image_path)

    if img is None:
        print("Error loading image.")
    else:
        belt, category = assign_belt(img)
        print(f"Detected object type: {category}")
        print(f"Assigned to Conveyor Belt {belt}")
