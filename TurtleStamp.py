#TurtleStamp
#Author: Tommy Shu
#Date: Mar 11, 2019

#Import turtle module
#Make a screen and turtle
#Name the turtle
#while ture:
#command: r = right(90)
#Command: l = left(90)
#Command: stop = break the function
#Command: s = stamp
#Command: f =forwad(10)
#Finish the program

#Make a turtle
import turtle
haha = turtle.Turtle()

#Do the following until the user type stop

while True:
    #Get the input from the user
    command=input("what should I do?\n")
    
    #If the user type stop, exit the loop
    if command =="stop" :
        break
    
    #If the user type f, forward 10
    if command =="f" :
        haha.forward (10)
        
    #If user type s, stamp
    if command =="s" :
        haha.stamp()
    
    #If user type l, turn left(90)
    if command =="l":
        haha.left(90)
        
    #If user type r, turn right(90)
    if command =="r":
        haha.right(90)
        
#finish the program
turtle.done()