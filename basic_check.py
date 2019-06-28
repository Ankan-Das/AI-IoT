import cv2
img = cv2.imread("Penguins.jpg",1)
img_1 = cv2.imread("Penguins.jpg",0)

print(img)
print(img_1)
print(type(img))
print(img.shape)

#resized_image = cv2.resize(img,(150,150))
resized_image2 = cv2.resize(img_1,(int(img_1.shape[1]/2),int(img_1.shape[1]/2)))

cv2.imshow("Penguins",resized_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
