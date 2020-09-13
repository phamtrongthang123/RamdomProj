import cv2 
import numpy as np 

# ref: https://stackoverflow.com/questions/58540100/remove-non-straight-lines-from-text-image  

# Read in image, cvt to grayscale, and apply Otsu's threshold to get 
image = cv2.imread('HOADONMAU.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Create diagonal kernel
kernel = np.array([[0, 0, 1],
                   [0, 1, 0],
                   [1, 0, 0]], dtype=np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

# noise will be created by apply kernel into character

# find contours
cnts, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # -> contours, hierarchy

# remove noise by contours
for c in cnts:
    area = cv2.contourArea(c)
    # tweak area to remove noise, tweak by hand
    if area < 100: 
        cv2.drawContours(opening, [c], -1, (0,0,0), -1) # just a way to draw

opening = cv2.merge([opening, opening, opening])
result = cv2.bitwise_xor(image, opening) # xor on 3 channel

cv2.imwrite('result.jpg', result) 