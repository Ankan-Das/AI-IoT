import cv2
import numpy as np

def canny(image):
	gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	canny = cv2.Canny(blur, 50, 150)
	return canny

def region_of_interest(image):
	height = image.shape[0]  #returns height of image
	polygons = np.array([
	[(150,height),(750,height),(450,250)]   #dimensions can be found from matplotlib and printing plt.imshow(<image>) and plt.show()
	])
	mask = np.zeros_like(image) #creates another image of same dimentions and pixels but black in color
	cv2.fillPoly(mask,polygons,255) #fills mask with polygons and with  	return mask
	masked_image = cv2.bitwise_and(image,mask)
	return masked_image

image = cv2.imread('/home/ankan/Desktop/Image_Process/photos/photo.jpg')
copy_image = np.copy(image)
canny = canny(copy_image)
cropped_image = region_of_interest(canny)
#lines = 
cv2.imshow("result", cropped_image)
cv2.waitKey(0)
