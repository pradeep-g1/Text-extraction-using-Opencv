import cv2
import pytesseract

# Read the image
image = cv2.imread("image1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
gray = cv2.medianBlur(gray, 3)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

filename = "output1.txt"
# Apply OCR using tesseract
text = pytesseract.image_to_string(gray, config='--psm 11 --oem 3')
# Write the OCR text to a file
with open(filename, 'w') as f:
    f.write(text)
