import cv2

#read in image
source_file = 'Nate-Chambers.jpg'
image = cv2.imread(source_file)
cv2.imshow('Prof', image)
cv2.waitKey(1000)
copy1 = image.copy()
copy2 = image.copy()
copy3 = image.copy()

#put leprechaun over Prof's face
source_file2 = 'leprechaun.png'
image2 = cv2.imread(source_file2)
image[30:180, 200:354] = image2
cv2.imshow('Prof', image)
cv2.waitKey(1000)

#Move Leprechaun
source_file2 = 'leprechaun.png'
image2 = cv2.imread(source_file2)
copy1[50:200, 220:374] = image2
cv2.imshow('Prof', copy1)
cv2.waitKey(1000)

source_file2 = 'leprechaun.png'
image2 = cv2.imread(source_file2)
copy2[70:220, 240:394] = image2
cv2.imshow('Prof', copy2)
cv2.waitKey(1000)

source_file2 = 'leprechaun.png'
image2 = cv2.imread(source_file2)
copy3[90:240, 260:414] = image2
cv2.imshow('Prof', copy3)
cv2.waitKey(1000)



cv2.destroyAllWindows()
