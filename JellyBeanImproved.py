#JellyBeanImproved
#Author: Tommy Shu
#Date: May 13, 2019



from PIL import Image
import time

#The first timing point
t0 = time.time()

#Open the image
file = Image.open("jelly_beans.jpg")

#Load the image
jb_image = file.load()

#Initialize colour pixels
yellow_pixels = 0
red_pixels = 0
green_pixels = 0
blue_pixels = 0
purple_pixels = 0

#Get size of the image
width = file.width
height = file.height

#Second timing point
t1 = time.time()

#Loop through all the pixels
for column in range(width):
  for row in range(height):
    
    #Define pixels
        pixel = jb_image[column, row]
 
       #Get the pixels rgb values 
        r = pixel [0]
        g = pixel [1]
        b = pixel [2]

    #Add on to the number if the colour is yellow
    if r>150 and g>150 and b<150:
      yellow_pixels+=1
      
    #Add on to the number if the colour is green
    elif r>150 and g<30 and b<30:
      red_pixels += 1
    
    #Add on to the number if the colour is blue
    elif r<45 and g>50 and b<45:
      green_pixels +=1
    
    #Add on to the number if the colour is red
    elif r<35 and g<35 and b>45:
      blue_pixels +=1
      
    #Add on to the number if the colour is purple
    elif r>100 and g<100 and b<120:
      purple_pixels +=1

#The third timing point
t2 = time.time()

#Calculate totall pixel number
total_pixels = width*height

#Calculate all colour ratios
yellow_ratio = 100*yellow_pixels/total_pixels
red_ratio = 100*red_pixels/total_pixels
green_ratio = 100*green_pixels/total_pixels
blue_ratio = 100*blue_pixels/total_pixels
purple_ratio = 100*purple_pixels/total_pixels

#Report of all the imformation
report = "There are {:.2f} % yellow jelly beans, {:.2f} % red jelly beans, {:.2f} % green jelly beans, {:.2f} % blue jelly beans and {:.2f} % purple jelly beans.".format(yellow_ratio, red_ratio, green_ratio, blue_ratio, purple_ratio)

#Print out report
print(report)

#The fourth timing point
t3 = time.time()

#Calculate time it takes the run the program
time_it_takes = "It takes {:.2f} seconds to genrate the final output and looping time is {:.2f} seconds.".format(t3-t0,t2-t1)

#Print out time it takes
print(time_it_takes)