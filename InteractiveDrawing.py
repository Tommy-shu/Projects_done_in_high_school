#InteractiveDrawing
#Author: Tommy Shu  
#Date: Mar 13, 2019

# allowed colour = ["red", "blue", "purple", "cyan", "turquoise", "thistle"]
#Create three functions determine the shape, size and the colour of the graph
#Make a question ask for input , size of the graph
#while answer_1 =="" or answer_1 != "allowed size ":
#print("Please give me a size between 100 and 200)
#return question_1
#while answer_1 ture
#Make a question ask for input, the colour filled in the graph ("Please give me a colour between blue, turquoise and yellow")
#while answer_2=="" or answer_2 !="allowed colour":
#print ("Please gice me a colour that is allowed")
#return question_2
#Call the function
#hide the turtle
#finish the program

import turtle
haha = turtle.Turtle()

#Function define the colour of the pen
def graph_colour (colour):
    """The function can determine the color of the pen we use for graph"""
    haha.color(colour)
    
#Function defines the shape
def graph_shape_size(angle,distance):
    """The function can change the graph shape size by changing the angle"""
    for move in range(300):
        haha.goto(0,0)
        haha.forward(distance)
        haha.left(angle)
        haha.forward(distance)
        haha.left(angle)

#Initialize variables
allowed_colour = ["red", "blue", "purple", "cyan", "turquoise", "thistle"]
        
#Ger and check for colour of the graph
colour=input("What colour do you want for your graph?(choose between red, blue, purple, cyan, turquoise, thistle)\n").lower().strip("!.")

while colour =="" or colour not in allowed_colour:
    colour=input("Nice choice! However, we don't have this colour,can you pick a colour that we have?\n").lower().strip("!.")
    if colour in allowed_colour:
        True
    else:
        False


#Get and check for degree
angle=float(input("What shape do you want for your graph? (Enter a degree that you want to turn left with)\n"))

#Get and check for size
distance=int(input("What size do you want for your graph? (Enter a number between 100 and 200) \n"))

while distance>200 or distance<100:
    distance=int(input("Please give me a distance between 100 and 200\n"))
    if distance>200 or distance<100:
        False
    else:
        True

#Set a speed for the function
haha.speed(500)

#Hide the turtle
haha.hideturtle()

#Call the function
graph_colour(colour)
graph_shape_size(angle,distance)
turtle.done()
