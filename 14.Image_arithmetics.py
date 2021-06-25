import cv2
import numpy as np
img=cv2.imread("ammi.jpg")
cv2.imshow("Negative",255-img)
cv2.imshow("Original",img)
cv2.waitKey(0)
M=np.ones(img.shape,dtype="uint8")*125
M1=np.zeros(img.shape,dtype="uint8")+0

added=cv2.add(img,M1)
subtract=cv2.subtract(img,M1)
multiply=cv2.multiply(img,0.5)
# added=cv2.add(img,M)
# subtract=cv2.subtract(img,M)
# multiply=cv2.multiply(img,M)
cv2.imshow("Added",added)
cv2.imshow("Subtract",subtract)
cv2.imshow("Multiply",multiply)


cv2.waitKey(0)
cv2.destroyAllWindows()
