import numpy as np
from PIL import Image

try:

    image1 = Image.open(input("Enter the name of the first image:\n"))
    image2 = Image.open(input("Enter the name of the second image:\n"))

except OSError:
        print('\nFailed to open image.\n')
        exit()

image_array1 = np.array(image1)
image_array2 = np.array(image2)

(width1, height1) = image1.size
(width2, height2) = image2.size

if(width1 != width2 or height1 != height2):
    print("The images have different sizes.\n")
    exit()

shape1 = image_array1.shape

for i in range(shape1[0]):
    for j in range (shape1[1]):
        if(image_array1[i][j][0] == image_array2[i][j][0] and image_array1[i][j][1] == image_array2[i][j][1] and image_array1[i][j][2] == image_array2[i][j][2]):
            
            image_array1[i][j][0] = 0
            image_array1[i][j][1] = 0
            image_array1[i][j][2] = 0
        else:
            image_array1[i][j][0] = 255
            image_array1[i][j][1] = 255
            image_array1[i][j][2] = 255

name = input("How to name the new image?\n")       

pil_image = Image.fromarray(image_array1)

pil_image.show()

pil_image.save(name)




