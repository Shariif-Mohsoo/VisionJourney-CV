import cv2

img = cv2.imread('triangle.jpg')
img = cv2.resize(img, (400, 400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 50, 200)
contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

print(f'Number of contours: {len(contours)}')

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    if len(approx) == 3:
        print('Triangle detected')
    elif len(approx) == 4:
        print('Quadrilateral detected')
    else:
        print('Other shape detected') 
    
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(img, f'Points: {len(approx)}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)


cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()