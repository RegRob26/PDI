# Python code to read image
import cv2

img = cv2.imread("CAT.jpg", 0)


cv2.imshow("image", img)


cv2.waitKey(0)


cv2.destroyAllWindows()

filename = 'CATNOTANGRY.jpg'
cv2.imwrite(filename, img)
print(img)