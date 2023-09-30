import cv2
import numpy as np

glasses = cv2.imread('imgs/glasses.jpg')
strawberry = cv2.imread('imgs/strawberry.jpg')
text1 = cv2.imread('imgs/lorem.jpg')
text2 = cv2.imread('imgs/fish.jpg')
INPUT = cv2.imread('imgs/glasses.jpg')

for i in range(4):
    if i == 0:
        INPUT = glasses
    elif i == 1:
        INPUT = strawberry
    elif i == 2:
        INPUT = text1
    elif i == 3:
        INPUT = text2

    filter = np.zeros_like(INPUT)
    filter[:] = (0, 0, 255)

    bwINPUT = cv2.cvtColor(INPUT, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(bwINPUT, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros_like(bwINPUT)

    cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)

    object_cut = cv2.bitwise_and(INPUT, INPUT, mask=mask)

    result = cv2.addWeighted(filter, 1, object_cut, 1, 0)

    if i == 0:
        cv2.imwrite('imgs/filtered_glasses.jpg', result)
    elif i == 1:
        cv2.imwrite('imgs/filtered_strawberry.jpg', result)
    elif i == 2:
        cv2.imwrite('imgs/filtered_text1.jpg', result)
    elif i == 3:
        cv2.imwrite('imgs/filtered_text2.jpg', result)