import cv2
import time
video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
lefteye_cascade = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
a=1
while True:
	a=a+1
	check,frame = video.read()
	gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
			# We use gray_img inside the function as using a colored image will be a complex task
	
	for x,y,w,h in faces:
		frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
	#for x,y,w,h in lefteyes:
	#	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
	frame=cv2.flip(frame,1)

	cv2.imshow('Capturing',frame)
	key=cv2.waitKey(1)
	if key==ord('q'):
		break
print(a)
video.release()
cv2.destroyAllWindows()
