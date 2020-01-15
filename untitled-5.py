from PIL import Image
import time

def colour(r,g,b):
    """Receives rgb values, determine the colour of the pixel and return the colour"""
    
    #If rgb value is in the range, return yellow
    if r>150 and g>150 and b<150:
        return "yellow"
    
    #If rgb value is in the range, return red
    elif r>150 and g<30 and b<30:
        return "red"
    
    #If rgb value is in the range, return green
    elif r<45 and g>50 and b<45:
        return "green"
    
    #If rgb value is in the range, return blue
    elif r<35 and g<35 and b>45:
        return "blue"
    
    #If rgb value is in the range, return purple
    elif r>100 and g<100 and b<120:
        return "purple"
    
    #If rgb value is in the range, return other
    else:
        return "other"
    
#Record the initial time
t0 = time.time()

#Open the image
file = Image.open("jelly_beans.jpg")

#Load the image
jb_image = file.load()

#Initialize different colour list
yellow_pixels = []
red_pixels = []
green_pixels = []
blue_pixels = []
purple_pixels = []

#Get size of the image
width = file.width
height = file.height

#Loop through all the pixels
for column in range(width):
    for row in range(height):
        
        #Define pixels
        pixel = jb_image[column, row]
 
       #Get the pixels rgb values 
        r = pixel [0]
        g = pixel [1]
        b = pixel [2]

    #Add on to the list if the colour is yellow
    if colour(r,g,b) != "other":
        position = (column, row)
        file.putpixel(position, (255,255,255))
        file.save("jellybeans.png""png")
    
    #Add on to the list if the colour is green
    if colour(r,g,b) == "green":
        green_pixels.append(pixel)
    
    #Add on to the list if the colour is blue
    if colour(r,g,b) == "blue":
        blue_pixels.append(pixel)
    
    #Add on to the list if the colour is red
    if colour(r,g,b) == "red":
        red_pixels.append(pixel)
    
    #Add on to the list if the colour is purple
    if colour(r,g,b) == "purple":
        purple_pixels.append(pixel)

#Get the length of list
yellow_number = len(yellow_pixels)
green_number = len(green_pixels)
red_number = len(red_pixels)
blue_number = len(blue_pixels)
purple_number = len(purple_pixels)

#Calculate totall pixel number
total_pixels = width*height

#Caluculate all colour ratio
yellow_ratio = 100*yellow_number/total_pixels
red_ratio = 100*red_number/total_pixels
green_ratio = 100*green_number/total_pixels
blue_ratio = 100*blue_number/total_pixels
purple_ratio = 100*purple_number/total_pixels

#Report of all the imformation
report = "There are {:.2f} % yellow jelly beans, {:.2f} % red jelly beans, {:.2f} % green jelly beans, {:.2f} % blue jelly beans and {:.2f} % purple jelly beans.".format(yellow_ratio, red_ratio, green_ratio, blue_ratio, purple_ratio)

#Print out report
print(report)

#Secong timing point
t1 = time.time()

#Calculate time it takes the run the program
time_it_takes = "It takes {:.2f} seconds to run my program.".format(t1-t0)

#Print out time it takes
print(time_it_takes)


