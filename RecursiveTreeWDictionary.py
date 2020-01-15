#Recursive Tree Dictionary
#Author: Tommy Shu
#Date: Apr 03,2019

#ALGORITHMN
#Create a function to draw a tree
#def tree_drawing(level, branch_length):
#    if level>0:
#        t.forward(branch_length)
#        t.right(40)
#        tree_drawing(level,branch_length/1.62)
#        level-=1
#        t.left(80)
#        tree_drawing(level,branch_length/1.62)
#        t.right(40)
#        t.back(brach_length)
#     else:
#        t.color(green)
#        t.stamp()
#        t.back("brown")
# set up drawing
#Create another function to put up and move the pen backward
#t.speed(0)
#t.up()
#t.goto(0,-180)
#t.left(90)
#t.down()
#Call the function

##########################CODE###########################
import turtle
t=turtle.Turtle()
myWin=turtle.Screen()

import random

#Define a function of drawing tree
def tree_drawing(level, branch_length):
    """draw a tree with three mini branches for each level"""
    
    if level>0:
        #Draw a branch
        t.forward(branch_length)
        
        #Turn right and draw a mini tree
        t.right(40)
        tree_drawing(level-1,branch_length/1.62)
        
        #Draw the middle mini tree
        t.left(40)
        tree_drawing(level-1,branch_length/1.62)
        
        #Turn left and draw a mini tree
        t.left(40)
        tree_drawing(level-1,branch_length/1.62)
        
        #Turn back angle
        t.right(40)
        t.back(branch_length)
        
#Drawing random color leave than turn back to brown color for branch
    else:
        t.color(dictonary[random_color])
        t.stamp()
        t.color("brown")
        
#Create a dictionary of colors
dictonary={"spring":"#FCB3F5", "summer": "#12C517","autumn":'#FFB533',"winter":'#BFF5F5',"nothing":'',"poison":'#050106'}

#Create a list of name of the color
lst=["spring","summer","autumn","winter","nothing","poison"]

#random number selection
random_number = random.randrange(1,6)

#Transfer from number to name of colors
random_color=lst[random_number]

#Move the turtle
t.speed(0)
t.penup()
t.goto(0,-180)
t.left(90)
t.pendown()

#Setup drawiong
t.color("brown")
t.width(3)
t.shape("triangle")

#Draw a tree
tree_drawing(4,120)

#Finish the program
myWin.exitonclick()
