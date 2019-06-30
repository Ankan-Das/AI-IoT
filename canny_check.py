import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #converts to grayscale, easy for further applications
	blur = cv2.GaussianBlur(gray, (5,5), 0)  #blurs the image to redce noise
	canny = cv2.Canny(blur, 50, 150)  #highlights the parts where there is a sudden change in itensity gradient
	return canny

image = cv2.imread('/home/ankan/Desktop/Image_Process/photos/photo.jpg')
copy_image = np.copy(image)
canny = canny(copy_image)


cv2.imshow("Hello", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
