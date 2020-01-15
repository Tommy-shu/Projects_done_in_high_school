#CombiningImages
#Date: Apr 17,2019
#Author: Tommy shu

#ALGORITHM
#Import image processing libraries/packages or modules
from PIL import Image

#Open the images files A (green screen) and B(background)
def is_green(r,g,b):
    if r>= 0 and r<25 and g>230 and g<=255 and b>=0 and b<25:
        return True
    else:
        return False
    
#Go through every green pixel in A and replace it with B
#Save the resulting image as C
