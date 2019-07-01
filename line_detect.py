import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
	gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	canny = cv2.Canny(blur, 50, 150)
	return canny

def region_of_interest(image):
	polygons = np.array([
	[(-200,900),(1400,900),(700,400)]
	])
	mask = np.zeros_like(image)
	cv2.fillPoly(mask,polygons,(255,255,255))
	masked_image = cv2.bitwise_and(image,mask)
	return masked_image

def display_lines(image,lines):
	line_image = np.zeros_like(image)
	if lines is not None:
		for line in lines:
			x1,y1,x2,y2 = line.reshape(4)
			cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),10)
	return line_image


image = cv2.imread('/home/ankan/Desktop/Image_Process/photos/car_lane.jpg')

canny_image = canny(image)
cropped_image = region_of_interest(canny_image)

lines = cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)

final = display_lines(image,lines)
combo_image = cv2.addWeighted(image,0.8,final,1,1)
cv2.imshow("capturing",combo_image)
cv2.waitKey(0)
#cv2.destroyAllWindows()


