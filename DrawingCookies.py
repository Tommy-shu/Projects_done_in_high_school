#Drawing cookies with function
#Author: Tommy Shu 
#Date:Mar 12, 2019

#Make the turtle
#Define a cookie drawing function
#draw the cookie edge
    #Chocolate chip in the middle
    #Chocolate chip on top left
    #Chocolate chip on bottom left
    #Chocolate chip on top right
    #Chocolate chip on bottom right
    #Call the cookie drawing function
#Finish the program

########################CODE###########################
#Make the turtle
import turtle
haha = turtle.Turtle()

#Define a cookie drawing function
def draw_cookie(x,y):
    """draw a cookie with chocolate chip on it"""
    #Draw the cookie outside
    haha.penup()
    haha.goto(-5 + x, -30 + y)
    haha.pendown()    
    haha.circle(30)
    haha.penup()
    
    #Chocolate chip in the middle
    haha.goto(0 + x,0 + y)
    haha.stamp()
    
    #Chocolate chip top left
    haha.goto(-10 + x, 10 + y)
    haha.stamp()
    
    #Chocolate chip bottom left
    haha.goto(-10 + x,-10 + y)
    haha.stamp()
    
    #Chocolate chip top right
    haha.goto(10 + x,-10 + y)
    haha.stamp()
    
    #Chocolate chip bottom left
    haha.goto(10 + x, 10 + y)
    haha.stamp()
    
#Use or "call" the function
draw_cookie(0,0)
draw_cookie(100,100)
draw_cookie(-70,30)

#Finish the program
turtle.done()