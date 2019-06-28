import cv2

lefteye_cascade = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("/home/ankan/Desktop/Image_Process/photos/tbbt_people.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

lefteyes = lefteye_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in lefteyes:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
for x,y,w,h in faces:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
