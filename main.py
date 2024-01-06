import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

# 1. İlk olaraq şəkil faylını Image, Grayscale, Blur rejimində oxuyuruq
img = cv2.imread('car1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

# 2. Sonra filtr tətbiq edirik və lokalizasiya üçün səkildə nömrənin sərhədlərini tapıriq
bfilter = cv2.bilateralFilter(gray, 11, 17, 17) # Noise azaldılması
edged = cv2.Canny(bfilter, 30, 200) #Sərhədlərin aşkarlanması
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

# 3. Konturları tapırıq və maska tətbiq edirik
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
        
        
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]


# 4. Nömrəni oxumaq üçün Easy OCR istifadə edirik
reader = easyocr.Reader(['az'])
result = reader.readtext(cropped_image)
number = result[0][-2] #Avtomobilin nömrəsini sətr formatında əldə edirik və number veriləninə təyin edirik
print(number)

