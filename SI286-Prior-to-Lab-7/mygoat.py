import cv2

source_file = 'goat.png'
image = cv2.imread(source_file)
blue = (255, 0, 0)
image[181, 148] = blue
gold = (0, 215, 255)

cv2.ellipse(image,(200,200),(200,100),0,0,360,255,-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'Censored',(50,225), font, 2,(0,0,0),4,cv2.LINE_AA)
cv2.circle(image, (380, 160), 10, gold, 3)
cv2.imshow('The Goat', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Under the top-right horn:", image[50, 350])
print("Inside the goatee", image[350, 205])

# I used OpenCV-Python Tutorials for help with syntax
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
