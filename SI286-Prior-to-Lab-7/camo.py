# I had the number of pixels changed increase to 300 so there were more blobs
# I had the blob clode block run 10 times instead of 15 so the blobs were smaller

import numpy as np     # names a variable 'np' for you to use
import cv2
import random

# Declare colors
grass = (76, 121, 82)
trees = (60, 86, 102)
sand = (115, 175, 187)
shadow = (63, 56, 53)

# Create a green grass image
grass_img = np.full ( (100, 150, 3), (76, 121, 82), np.uint8)

# Chane 80 pixels in the image to different colors, corresponding to previous variables
for x in range(300):
    xcord = random.randrange(150)
    ycord = random.randrange(100)
    material = int(random.randrange(3))
    if material == 0:
        material = trees
    elif material == 1:
        material = sand
    elif material == 2:
        material = shadow
    grass_img[ycord, xcord] = material

# Turn boxes into blobs by having the program check for green
# and turn green dots into a different color.
for x in range(10):
    for ycord in range(100):
        for xcord in range(150):
            if grass_img[ycord, xcord, 0] == grass[0]:
                new_color = int(random.randrange(4))
                if (new_color == 0) and ((ycord + 1) <= 99):
                    grass_img[ycord, xcord] = grass_img[(ycord + 1), (xcord)]
                elif (new_color == 1) and ((xcord + 1) <=149):
                    grass_img[ycord, xcord] = grass_img[(ycord), (xcord + 1)]
                elif (new_color == 2) and ((ycord - 1) >= 0):
                    grass_img[ycord, xcord] = grass_img[(ycord - 1), (xcord)]
                elif (new_color == 3) and ((xcord -1) >= 0):
                    grass_img[ycord, xcord] = grass_img[(ycord), (xcord - 1)]
                else:
                    continue
            else:
                continue

# Print image size and show the new image with changed pixels
print(grass_img.shape)
cv2.imshow('grass', grass_img)
cv2.waitKey(0)

# Resize the image to 5 times its original size
grass_img = cv2.resize(grass_img, (750, 500), interpolation=cv2.INTER_NEAREST)
cv2.imshow('camo', grass_img)
cv2.waitKey(0)
